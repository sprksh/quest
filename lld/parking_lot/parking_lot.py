import datetime


"""
parking lot

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

"""


class Parking:
    def __init__(self, vehicle_number, parking_slot):
        self.vehicle_number = vehicle_number
        self.parking_slot = parking_slot
        self.in_time = datetime.datetime.now()
        self.out_time = None
        self.bill_amount = 0

    def exit(self):
        self.out_time = datetime.datetime.now()
        bill_amount = self.calculate_bill()
        self.bill_amount = bill_amount
        return bill_amount

    def calculate_bill(self):
        duration = self.out_time - self.in_time
        rate = 0
        if duration <= datetime.timedelta(seconds=60*60*2):
            rate = self.parking_slot.rate_dict["<2"]
        if datetime.timedelta(seconds=60*60*2) < duration <= datetime.timedelta(seconds=60*60*4):
            rate = self.parking_slot.rate_dict["2-4"]
        if datetime.timedelta(seconds=60*60*4) < duration <= datetime.timedelta(seconds=60*60*8):
            rate = self.parking_slot.rate_dict["4-8"]
        if datetime.timedelta(seconds=60*60*8) < duration:
            rate = self.parking_slot.rate_dict[">8"]
        return rate


class ParkingSlot:
    def __init__(self, id, vehicle_type, rate_dict):
        self.id = id
        self.vehicle_type = vehicle_type
        self.parkings = []
        self.current_parking = None
        self.rate_dict = rate_dict

    def park_vehicle(self, vehicle_number):
        parking = Parking(vehicle_number, self)
        self.current_parking = parking
        self.parkings.append(parking)
        return self.id

    def exit_slot(self):
        bill_amount = self.current_parking.exit()
        self.current_parking = None
        return bill_amount

    @staticmethod
    def parking_lot_factory(id, vehicle_type, rate_dict):
        return ParkingSlot(id, vehicle_type, rate_dict)



"""

VehicleTye(Enum)


PeriodRange




Rate
    vehicle_type
    period_range: int
    cost: float
    paking_lot


ParkingLotCapacity
    parking_lot_id
    vehicle_type
    max_capacity

Parking Lot
    id
    
Parking Slot
    id
    parking_lot_id
    vehicle_type
    full : bool 
    vehicle_number
    

ParkingPosition:
    vehicle_number
    parking_slot_id
    exited = 


Parking:
    vehicle_number
    parking_slot_id
    current = True


combo
    vehicle_number
    parking_slot_id

db table: parking_lot_id_in_process_of_creating_parking_entry: False
    
assign parking slot to new vehicle:
    1. check if slot is available
        sql transaction:
            2. check if vehicle is there in the parking
            3. check if slot is there in parking
            4. create combo (vehicle_number, parking_slot_id)
        
    if combo there block
    



Parking:
    vehicle_number
    parking_slot_id
    current: bool
    in_time
    out_time
    bill_amount
    
"""

class ParkingLot:
    def __init__(self, id, capacity_dict: dict, rate_dict: dict):
        self.id = id
        self.capacity_dict = capacity_dict
        self.rate_dict = rate_dict
        self.current_capacity = capacity_dict.copy()
        self.parking_lot_dict = {}
        self.prepare_parking_lot()
        self.vehicle_position_dict = {}
        # self.lock = threading.Lock()

    def prepare_parking_lot(self):
        for vehicle_type, count in self.capacity_dict.items():
            self.parking_lot_dict[vehicle_type] = []
            rate_dict = self.rate_dict[vehicle_type]
            for i in range(count):
                self.parking_lot_dict[vehicle_type].append(ParkingSlot.parking_lot_factory(id, vehicle_type, rate_dict))

    def find_empty_spot(self, vehicle_type) -> ParkingSlot:
        if not self.current_capacity[vehicle_type]:
            print("N0 empty space")
            return None
        for slot in self.parking_lot_dict[vehicle_type]:
            if not slot.current_parking:
                return slot

    def park_vehicle(self, vehicle_number, vehicle_type):
        # with self.lock:
        slot = self.find_empty_spot(vehicle_type)
        slot_id = None
        if slot:
            self.current_capacity[vehicle_type] -= 1
            slot_id = slot.park_vehicle(vehicle_number)
        self.vehicle_position_dict[vehicle_number] = slot
        return slot_id

    def exit(self, vehicle_number):
        slot = self.vehicle_position_dict.get(vehicle_number)
        if slot:
            bill_amount = slot.exit_slot()
            print("Payable: %s" % str(bill_amount))
            return bill_amount
        print("Sorry! No vehicle found")
        return
