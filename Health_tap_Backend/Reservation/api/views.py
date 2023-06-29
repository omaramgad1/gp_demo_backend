from rest_framework.decorators  import  api_view, permission_classes
from rest_framework.response import Response
from Reservation.models import Reservation
from Appointment.models import Appointment
from User.models import Patient
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_reservation(request):
    print ('********************************')
    print (request.user)
    print ('********************************')
    patient = get_object_or_404(Patient , user = request.user)
    reservations = Reservation.objects.filter(patient=patient)
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_reserved_reservation(request):
    patient = get_object_or_404(Patient , user = request.user)
    reservations = Reservation.objects.filter( patient=patient, status='R')
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def list_cancelled_reservation(request):
#     reservations = Reservation.objects.filter(status='C')
#     serializer = ReservationSerializer(reservations, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_done_reservation(request):
    patient = get_object_or_404(Patient , user = request.user)
    reservations = Reservation.objects.filter( patient=patient, status='D')
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_specific_reservation(request, reservation_id):
    patient = get_object_or_404(Patient , user = request.user)
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id, patient=patient)
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_reservation(request, appointment_id):
    patient = get_object_or_404(Patient, user=request.user)
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if appointment.status == 'A':
        reservation = Reservation.objects.create(patient=patient, appointment=appointment, status='R')
        appointment.status = 'R'
        appointment.save()
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    return Response({'message': 'Appointment is not available.'}, status=status.HTTP_400_BAD_REQUEST)
