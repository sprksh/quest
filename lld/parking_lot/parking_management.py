from parking_lot import ParkingLot


class ParkingManagementService:
    def __init__(self):
        self.parking_lot_dict = {}

    def register_parking_lot(self, id, parking_lot):
        self.parking_lot_dict[id] = parking_lot

    def create_parking_lot(self):
        capacity_dict = {
            "two_wheeler": 30,
            "hatchback": 20,
            "suv": 5
        }

        rate_dict = {
            "two_wheeler": {"<2": 20, "2-4": 30, "4-8": 50, ">8": 100},
            "hatchback": {"<2": 20, "2-4": 30, "4-8": 50, ">8": 100},
            "suv": {"<2": 20, "2-4": 30, "4-8": 50, ">8": 100},
        }

        id = len(self.parking_lot_dict) + 1
        parking_lot = ParkingLot(id, capacity_dict, rate_dict)
        self.register_parking_lot(id, parking_lot)

    def park(self, parking_lot_id, vehicle_number, vehicle_type):
        parking_lot = self.parking_lot_dict[parking_lot_id]
        slot_id = parking_lot.park_vehicle(vehicle_number, vehicle_type)
        return slot_id

    def exit(self, parking_lot_id, vehicle_number):
        parking_lot = self.parking_lot_dict[parking_lot_id]
        bill_amount = parking_lot.exit(vehicle_number)
        return bill_amount
