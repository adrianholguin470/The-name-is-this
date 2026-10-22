# Meeting SMS reminders (30 min + 5 min before)

Texts Adrian 30 minutes and 5 minutes before every timed Google Calendar meeting.

## How it works

- A Claude Routine runs hourly at :05.
- It reads Google Calendar (primary) for meetings starting in the *next* clock hour.
- For each meeting it schedules two SMS through HighLevel (sub-account "Holguin & Company")
  using the `send-a-new-message` operation with `scheduledTimestamp`, so HighLevel delivers
  the texts at exactly T-30 and T-5 even if no session is running at that moment.
- Idempotency keys `mtg-<eventId>-30` / `mtg-<eventId>-5` prevent duplicate texts.

Recipient: HighLevel contact `EXu13w6lnK2VYGRI3RFf` in location `hLql8kZCEo7GMT34NQdL`
(Adrian's own record, phone ending 3607). Change the contact id to change the number.

## Known limits

- Meetings created or moved less than ~1 hour before they start are missed by the hourly sweep.
- All-day events and declined invites are skipped.
- If the routine ever needs to be recreated in the claude.ai Routines UI, attach the
  **Google Calendar** and **HighLevel CannaShark Holguin** connectors and paste the prompt below.

## Routine prompt (standalone version)

```
You are an automated meeting-reminder job for Adrian Holguin (adrian.holguin.470@gmail.com).
Schedule SMS reminders 30 min and 5 min before each meeting starting in the NEXT clock hour.

1. Run `date -u +%s`, round DOWN to the top of the current hour = H.
   Window: meeting start >= H+3600 and < H+7200.
2. Google Calendar list_events on the primary calendar with startTime/endTime = H+3600 and
   H+7200 as Pacific-time ISO strings, no offset, no Z
   (TZ=America/Los_Angeles date -d @<epoch> +%Y-%m-%dT%H:%M:%S).
   Keep only events with start.dateTime, status confirmed, and self attendee not "declined".
   If none, end quietly.
3. For each meeting with start epoch S, call HighLevel execute_operation
   operationId send-a-new-message, locationId hLql8kZCEo7GMT34NQdL, twice:
   - idempotencyKey mtg-<eventId>-30, body {"type":"SMS","contactId":"EXu13w6lnK2VYGRI3RFf",
     "message":"Reminder: '<title>' starts in 30 min (<h:mm AM/PM> PT). <join link>",
     "scheduledTimestamp": S-1800}
   - idempotencyKey mtg-<eventId>-5, same but "in 5 min" and scheduledTimestamp S-300.
   Join link: conferenceUrl, else a Zoom/Teams/Meet URL from the description, else location.
   Never text any other contact; never more than two texts per meeting.
4. On success end with one line naming the meetings scheduled. On failure retry once, then
   report the error in one line.
```
