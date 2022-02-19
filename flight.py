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
                'Status: '+ self.status + '\n'
                )