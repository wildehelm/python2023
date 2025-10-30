# *** 120_Date and time - Datum und Zeit ***
# 2023-02-23

from datetime import datetime
# oder nur "import datetime", aber dann muss du "datetime.datetime..." benutzen

# now ISO 8601 Format
print('date-time... now')
jetzt = datetime.now()
print(jetzt)                # z. B. 2023-02-23 13:38:25.864733

# datetime()
# Konstruktor der datetime class
print('date-time... datetime')
geburtstag = datetime(1970, 12, 3, 12, 0, 0)
print(geburtstag)           # z. B. 1970-12-03 12:00:00

# time
print('date-time... time')
print(jetzt.time())         # z. B. 13:38:25.864733

# timestamp
print('date-time... timestamp...')
# UNIX-Timestamp
# Sekunden seit 1970-01-01
print('current timestamp:\t_\t_\t_\t_\t_\t-\t_\t', jetzt.timestamp())        # z. B. 1_677_156_049.781511
print('timestamp of a given day:\t_\t_\t_\t_\t_\t', geburtstag.timestamp())   # z. B. 29_070_000.0
print('n seconds between two dates:\t_\t_\t_\t_\t', jetzt.timestamp() - geburtstag.timestamp())
print('n seconds converted to hours:\t_\t_\t_\t_\t', (jetzt.timestamp() - geburtstag.timestamp()) / 60 / 60 / 24)               # z. B. 19075.08276570677
print('n seconds converted to hours:\t_\t_\t_\t_\t', (jetzt.timestamp() - geburtstag.timestamp()) / 60 / 60 / 24 / 365.25)      # z. B. 52.224730364700264
print('n seconds since the lecturer came to us:\t_\t', jetzt.timestamp() - datetime(2023, 2, 20, 8, 30, 0, 0).timestamp())
print()
print('date - n seconds from \'UNIX-Time Zero\'\t_\t_\t_', datetime.fromtimestamp(29070000.0))   # 1970-12-03 12:00:00
print('q:\t_\t_\t_\t_\t_\t_\t_\t_', datetime.fromtimestamp(0))            # 1970-01-01 01:00:00

print('r:\t_\t_\t_\t_\t_\t_\t_\t_', (2 ** 32) / 2 - 1)                            # 2147483647.0
print('s:\t_\t_\t_\t_\t_\t_\t_\t_', datetime.fromtimestamp((2 ** 32) / 2 - 1))    # 2038-01-19 04:14:07
print('Das erste spannende nach Y2K... der 19. Januar 2038 04:14 Uhr')