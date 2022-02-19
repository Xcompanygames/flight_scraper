class flightObject:
    def __init__(self, flight_company='', flight='', landing_from='', terminal='', scheduled_time='', updated_time='',
                 status=''):
        self.flight_company = flight_company
        self.flight = flight
        self.landing_from = landing_from
        self.terminal = terminal
        self.scheduled_time = scheduled_time
        self.updated_time = updated_time
        self.status = status

    def __str__(self):
        return ('Flight company: ' + self.flight_company + '\n' +
                'Flight: ' + self.flight + '\n' +
                'landing from: ' + self.landing_from + '\n' +
                'Terminal: ' + self.terminal + '\n' +
                'Scheduled Time: ' + self.scheduled_time + '\n' +
                'Updated Time: ' + self.updated_time + '\n' +
                'Status: ' + self.status + '\n'
                )

    def string_in_object(self, string):
        if string in self.flight_company:
            return True
        elif string in self.flight:
            return True
        elif string in self.landing_from:
            return True
        elif string in self.status:
            return True
        else:
            return False

    def search_terminal(self, num):
        if num in self.terminal:
            return True
        else:
            return False

    def search_updated_time(self, time):
        if time in self.updated_time:
            return True
        else:
            return False

    def search_scheduled_time(self, time):
        if time in self.scheduled_time:
            return True
        else:
            return False
