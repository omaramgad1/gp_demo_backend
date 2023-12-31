from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Reservation.models import Reservation
from Appointment.models import Appointment
from Patient.models import Patient
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import status
from Reservation.pagination import ReservedListPagination
from Health_tap_Backend.permissions import IsDoctor, IsPatient


@api_view(['GET'])
@permission_classes([IsPatient])
def list_all_reservation(request):
    patient = request.user.patient
    reservations = Reservation.objects.filter(patient=patient).order_by(F('appointment__date').desc(), F('appointment__start_time').desc())
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsPatient])
def list_reserved_reservation(request):
    # patient = get_object_or_404(Patient , user = request.user)
    patient = request.user.patient
    reservations = Reservation.objects.filter(patient=patient, status='R')
    paginator = ReservedListPagination()
    paginated_list = paginator.paginate_queryset(reservations, request)
    serializer = ReservationSerializer(reservations, many=True)
    return paginator.get_paginated_response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def list_cancelled_reservation(request):
#     reservations = Reservation.objects.filter(status='C')
#     serializer = ReservationSerializer(reservations, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsPatient])
def list_done_reservation(request):
    patient = request.user.patient
    reservations = Reservation.objects.filter(patient=patient, status='D')
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsPatient])
def list_specific_reservation(request, reservation_id):
    patient = request.user.patient
    reservation = get_object_or_404(
        Reservation, id=reservation_id, patient=patient)
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_reservation(request, appointment_pk):
#     patient = get_object_or_404(Patient, user=request.user)
#     print(patient)
#     print("********************************")
#     appointment = get_object_or_404(Appointment, id=appointment_pk)
#     print(appointment)
#     print(appointment.status)
#     print("********************************")
#     if appointment.status == 'A':
#         reservation = Reservation.objects.create(patient=patient, appointment=appointment, status='R')
#         appointment.status = 'R'
#         appointment.save()
#         serializer = ReservationSerializer(reservation)
#         return Response(serializer.data)

#     return Response({'message': 'Appointment is not available.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsPatient])
def create_reservation(request, appointment_pk):
    patient = request.user.patient
    appointment = get_object_or_404(Appointment, pk=appointment_pk, status='A')

    # Check if the patient has any existing reservations that have the same duration and overlapping time slots
    existing_reservations = Reservation.objects.filter(
        patient=patient,
        appointment__start_time__lt=appointment.end_time(),
        # appointment__end_time__gt=appointment.start_time,
        # appointment__duration=appointment.duration
        appointment__date=appointment.date
    )
    for e in existing_reservations: 
        if e.appointment.end_time() > appointment.start_time :
           return Response({'detail': 'Cannot reserve multiple appointments with the same duration and overlapping time slots'}, status=status.HTTP_400_BAD_REQUEST) 
        

    appointment.status = 'R'
    appointment.save()

    # Create a new reservation
    reservation = Reservation(
        patient=patient, appointment=appointment, status='R')
    reservation.save()

    serializer = ReservationSerializer(reservation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsPatient])
def delete_reservation(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    appointment = reservation.appointment

    reservation.delete()

    if not Reservation.objects.filter(appointment=appointment).exists():
        appointment.status = 'A'
        appointment.save()

    return Response({'message': 'Reservation deleted successfully.'})


@api_view(['PATCH'])
@permission_classes([IsPatient])
def cancel_reservation(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    appointment = reservation.appointment

    reservation.delete()

    if not Reservation.objects.filter(appointment=appointment).exists():
        appointment.status = 'A'
        appointment.save()

    return Response({'message': 'Reservation canceled successfully.'})
