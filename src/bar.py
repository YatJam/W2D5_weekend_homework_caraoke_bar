class Bar:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.entry_fee = 4.00
        self.till = 500.00
        self.waiting_list = []
        self.bar_area = []

    def guest_checkin(self, guest):
        self.room.guests_in_karaoke_room.extend(guest)
    
    def add_to_waiting_list(self, guest):
        self.waiting_list.extend(guest)

    def add_to_bar_area(self, guest):
        self.bar_area.append(guest)

    def check_guests_in_karaoke_room(self):
        return len(self.room.guests_in_karaoke_room)

    def check_waiting_list(self):
        return len(self.waiting_list)

    def check_bar_area(self):
        return len(self.bar_area)

    def add_payment_to_till(self, amount):
        self.till += amount

    def check_till_balance(self):
        return self.till

    def add_guests_to_capacity(self, guests):
        for guest in guests:
            if len(self.room.guests_in_karaoke_room) < self.room.capacity:
                self.guest_checkin([guest])
            else:
                self.add_to_waiting_list([guest])

    def pay_entry_fee_and_enter_karaoke_bar_if_space_available(self, guests):
        pending_guests = []
        for guest in guests:
            if guest.coin_purse >= self.entry_fee:
                guest.coin_purse -= self.entry_fee
                self.add_payment_to_till(self.entry_fee)
                self.add_guests_to_capacity([guest])
            else:
                 self.bar_area.append(guest)
        
        


