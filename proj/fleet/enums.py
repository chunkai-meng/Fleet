STATUS_DELETED = -1
COMMON_EXPIRED_DAYS = 30

MSG_NOT_FOUND = 'Not Found'

ROLE_STAFF = 0
ROLE_ADMIN = 1

JOBIDINFO_STATUS_CHOICES = (
    (1, 'Normal'),
    (-1, 'Deleted')
)

USERINFO_ROLE_CHOICES = (
    (0, 'Staff'),
    (1, 'Admin'),
    (-1, 'Deleted')
)

INFRINGEMENT_STATUS_UNPAID = 0
INFRINGEMENT_STATUS_PAID = 1
INFRINGEMENT_STATUS_CHOICES = (
    (INFRINGEMENT_STATUS_UNPAID, 'Unpaid'),
    (INFRINGEMENT_STATUS_PAID, 'Paid'),
    (-1, 'Deleted')
)

WORKSHOP_STATUS_CHOICES = JOBIDINFO_STATUS_CHOICES

VEHICLE_STATUS_SOLD = 3
VEHICLE_STATUS_IN_SERVICE = 2
VEHICLE_STATUS_BOOKED = 0
VEHICLE_STATUS_AVAILABLE = 1
VEHICLE_STATUS_DELETED = -1

VEHICLE_STATUS_CHOICES = (
    (VEHICLE_STATUS_BOOKED, 'Booked'),
    (VEHICLE_STATUS_AVAILABLE, 'Available'),
    (VEHICLE_STATUS_DELETED, 'Deleted'),
    (VEHICLE_STATUS_IN_SERVICE, 'InService'),
    (VEHICLE_STATUS_SOLD, 'SOLD')
)

SERVICE_STATUS_PROCESSING = 0
SERVICE_STATUS_COMPLETED = 1
SERVICE_STATUS_DELETE = -1
SERVICE_STATUS_CHOICES = (
    (SERVICE_STATUS_PROCESSING, 'Processing'),
    (SERVICE_STATUS_COMPLETED, 'Completed'),
    (SERVICE_STATUS_DELETE, 'Deleted'),
)
