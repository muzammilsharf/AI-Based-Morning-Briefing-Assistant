import os.path
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# IMPORTANT: This must match the scope you set in the Google Cloud Console
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_events():
    creds = None
    
    # 1. The code looks for 'token.json' first (it won't exist yet)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # 2. If no token, use 'credentials.json' to log in via browser
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("Error: 'credentials.json' file not found in this folder!")
                return
            
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 3. Save the token for the next time so we don't have to log in again
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Connect to the Google Calendar service
        service = build('calendar', 'v3', credentials=creds)

        # Get the current time in UTC
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print('Connecting to Google Calendar...')
        
        # Pull the next 5 events
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=5, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('Connection Success, but no upcoming events found.')
            return

        print("\n--- YOUR CALENDAR DATA ---")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(f"- {event.get('summary')} at {start}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    get_calendar_events()