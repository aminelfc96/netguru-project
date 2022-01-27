
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import cars, rate
from .serializers import CarsSerializer, RateSerializer
from .api import ApiCallToVerifyVehicle


class Home(APIView):
    def get(self, request):
        return Response({"status": "is running"})


class ShowAddCars(APIView):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM main_api_cars 
        ORDER BY main_api_cars.id ASC
        """)
        data = cursor.fetchall()
        sort = []

        for row in data:
            sort.append({
                "id": row[0],
                "make": row[1],
                "model": row[2],
                "avg_rate": row[3],
            })
        return Response(sort)

    def post(self, request, *args, **kwargs):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            if ApiCallToVerifyVehicle(request.data["make"], request.data["model"]).DoesExist():
                if cars.objects.filter(make=request.data["make"], model=request.data["model"]).exists():
                    return Response({"message": "element already exist"})
                else:
                    serializer.save()
                    return Response(serializer.data)
            else:
                return Response({"message": "error"})
        return Response(serializer.errors)


class DeleteCar(APIView):
    def delete(self, request, id):
        try:
            to_be_deleted = cars.objects.get(id=id)
            to_be_deleted.delete()
            return Response({"message": "element deleted"})
        except:
            return Response({"message": "element not found"})


class AddRates(APIView):

    def post(self, request, *args, **kwargs):

        serializer = RateSerializer(data=request.data)

        if serializer.is_valid():
            if cars.objects.filter(id=request.data["car_id"]).exists():
                if not rate.objects.filter(car_id=request.data["car_id"]).exists():
                    serializer.save()
                car_rate = rate.objects.get(car_id=request.data["car_id"])
                car_rate.sum_rate += request.data["rating"]
                car_rate.rates_number += 1
                car_rate.save()

                update_avg = cars.objects.get(id=request.data["car_id"])
                update_avg.avg_rate = round(car_rate.sum_rate/car_rate.rates_number, 1)
                update_avg.save()
                return Response(serializer.data)
            return Response({"error": "element not found"}, status=404)

        return Response(serializer.errors)


class ShowPopular(APIView):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("""SELECT main_api_cars.ID,main_api_cars.make,main_api_cars.model,main_api_rate.rates_number
                         FROM main_api_cars
                         JOIN main_api_rate ON main_api_cars.id=main_api_rate.car_id_id
                         ORDER BY main_api_rate.rates_number DESC""")
        data = cursor.fetchall()
        sort = []
        for row in data:
            sort.append({
                "id": row[0],
                "make": row[1],
                "model": row[2],
                "rates_number": row[3],
            })
        return Response(sort)

