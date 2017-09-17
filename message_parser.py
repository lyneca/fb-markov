from html.parser import HTMLParser

class BaseMessageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.state = 0
        '''
        States:
         0: New thread name list
         1: Name of sender
         2: Time sent
         3: Message
        '''

    def handle_starttag(self, tag, attrs):
        attrs = {x[0]: x[1] for x in attrs}
        if not 'class' in attrs and not tag == 'p':
            return

        if tag == 'p':
            self.state = 3
        elif attrs['class'] == 'meta':
            self.state = 2
        elif attrs['class'] == 'thread':
            self.state = 0
        elif attrs['class'] == 'user':
            self.state = 1

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        data = data.strip()
        if self.state == 0:
            self.handle_users(', '.split(data))
        elif self.state == 1:
            self.handle_sender(data)
        elif self.state == 2:
            self.handle_timestamp(data)
        else:
            self.handle_message(data)

    def handle_timestamp(self, timestamp):
        pass

    def handle_message(self, message):
        pass

    def handle_sender(self, sender):
        pass

    def handle_users(self, users):
        pass