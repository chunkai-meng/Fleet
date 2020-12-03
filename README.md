# Fleet Django Backend

[toc]

## infringement

### list

GET `/api/infringement/`



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/infringement/`



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                         | Description |
| :-------------------------------- | :---------- |
| `Cdate`                           |             |
| `InfringementNumber` **required** |             |
| `PlateNumber` **required**        |             |
| `Amount`                          |             |
| `Date`                            |             |
| `UserID`                          |             |
| `PaidDate`                        |             |
| `OriginalID`                      |             |
| `Status` **required**             |             |


### read

GET `/api/infringement/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                           |
| :---------------- | :---------------------------------------------------- |
| `id` **required** | A unique integer value identifying this infringement. |



### update

PUT `/api/infringement/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                           |
| :---------------- | :---------------------------------------------------- |
| `id` **required** | A unique integer value identifying this infringement. |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                         | Description |
| :-------------------------------- | :---------- |
| `Cdate`                           |             |
| `InfringementNumber` **required** |             |
| `PlateNumber` **required**        |             |
| `Amount`                          |             |
| `Date`                            |             |
| `UserID`                          |             |
| `PaidDate`                        |             |
| `OriginalID`                      |             |
| `Status` **required**             |             |



### partial_update

PATCH `/api/infringement/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                           |
| :---------------- | :---------------------------------------------------- |
| `id` **required** | A unique integer value identifying this infringement. |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter            | Description |
| :------------------- | :---------- |
| `Cdate`              |             |
| `InfringementNumber` |             |
| `PlateNumber`        |             |
| `Amount`             |             |
| `Date`               |             |
| `UserID`             |             |
| `PaidDate`           |             |
| `OriginalID`         |             |
| `Status`             |             |



### delete

DELETE `/api/infringement/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                           |
| :---------------- | :---------------------------------------------------- |
| `id` **required** | A unique integer value identifying this infringement. |



## job-code

 Interact

### list

GET `/api/job-code/`



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/job-code/`



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter         | Description |
| :---------------- | :---------- |
| `JobName`         |             |
| `JobAbbreviation` |             |
| `Status`          |             |



### read

GET `/api/job-code/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `id` **required** | A unique integer value identifying this job id info. |



### update

PUT `/api/job-code/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `id` **required** | A unique integer value identifying this job id info. |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter         | Description |
| :---------------- | :---------- |
| `JobName`         |             |
| `JobAbbreviation` |             |
| `Status`          |             |



### partial_update

PATCH `/api/job-code/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `id` **required** | A unique integer value identifying this job id info. |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter         | Description |
| :---------------- | :---------- |
| `JobName`         |             |
| `JobAbbreviation` |             |
| `Status`          |             |



### delete

DELETE `/api/job-code/{id}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `id` **required** | A unique integer value identifying this job id info. |



## service-form


### list

GET `/api/service-form/`



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/service-form/`



All Fields are **required** except for **'SN'**



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                   | Description |
| :-------------------------- | :---------- |
| `WorkshopID` **required**   |             |
| `PlateNumber` **required**  |             |
| `ServiceName` **required**  |             |
| `ServicePrice` **required** |             |
| `StartDate` **required**    |             |
| `EndDate` **required**      |             |



### read

GET `/api/service-form/{SN}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description |
| :---------------- | :---------- |
| `SN` **required** |             |



### update

PUT `/api/service-form/{SN}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description |
| :---------------- | :---------- |
| `SN` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                   | Description |
| :-------------------------- | :---------- |
| `WorkshopID` **required**   |             |
| `PlateNumber` **required**  |             |
| `ServiceName` **required**  |             |
| `ServicePrice` **required** |             |
| `StartDate` **required**    |             |
| `EndDate` **required**      |             |


### partial_update

PATCH `/api/service-form/{SN}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description |
| :---------------- | :---------- |
| `SN` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter      | Description |
| :------------- | :---------- |
| `WorkshopID`   |             |
| `PlateNumber`  |             |
| `ServiceName`  |             |
| `ServicePrice` |             |
| `StartDate`    |             |
| `EndDate`      |             |



### delete

DELETE `/api/service-form/{SN}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description |
| :---------------- | :---------- |
| `SN` **required** |             |



## staffs


### list

GET `/api/staffs/`




### me

GET `/api/staffs/me/`



Get current user detail



## user-info


### list

GET `/api/user-info/`



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/user-info/`



All Fields are **required** (所有字段必填)



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                     | Description |
| :---------------------------- | :---------- |
| `SAMAccountName` **required** |             |
| `DepartmentID` **required**   |             |
| `DriverLicense` **required**  |             |
| `EmailAddress` **required**   |             |
| `LicenseClass` **required**   |             |
| `LicenseExpiryDate`           |             |
| `Mobile` **required**         |             |
| `Role`                        |             |



### read

GET `/api/user-info/{UserID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter             | Description |
| :-------------------- | :---------- |
| `UserID` **required** |             |



### update

PUT `/api/user-info/{UserID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter             | Description |
| :-------------------- | :---------- |
| `UserID` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                     | Description |
| :---------------------------- | :---------- |
| `SAMAccountName` **required** |             |
| `DepartmentID` **required**   |             |
| `DriverLicense` **required**  |             |
| `EmailAddress` **required**   |             |
| `LicenseClass` **required**   |             |
| `LicenseExpiryDate`           |             |
| `Mobile` **required**         |             |
| `Role`                        |             |



### partial_update

PATCH `/api/user-info/{UserID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter             | Description |
| :-------------------- | :---------- |
| `UserID` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter           | Description |
| :------------------ | :---------- |
| `SAMAccountName`    |             |
| `DepartmentID`      |             |
| `DriverLicense`     |             |
| `EmailAddress`      |             |
| `LicenseClass`      |             |
| `LicenseExpiryDate` |             |
| `Mobile`            |             |
| `Role`              |             |



### delete

DELETE `/api/user-info/{UserID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter             | Description |
| :-------------------- | :---------- |
| `UserID` **required** |             |



## vehicle-booking


### list

GET `/api/vehicle-booking/`



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/vehicle-booking/`



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter            | Description |
| :------------------- | :---------- |
| `Status`             |             |
| `Cdate`              |             |
| `SN`                 |             |
| `BookingStartAt`     |             |
| `BookingEndAt`       |             |
| `DepartmentID`       |             |
| `JobCodeID`          |             |
| `UserID`             |             |
| `VehicleID`          |             |
| `BookingReason`      |             |
| `BookingNotes`       |             |
| `AdminNotes`         |             |
| `MaintenanceBooking` |             |
| `StartedMileage`     |             |
| `ReturnedMileage`    |             |
| `ReturnedDate`       |             |
| `ReturnNote`         |             |
| `Clean`              |             |
| `DamageInfo`         |             |
| `Image`              |             |
| `OriginalID`         |             |



### my_bookings

GET `/api/vehicle-booking/my_bookings/`




### read

GET `/api/vehicle-booking/{SN}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description |
| :---------------- | :---------- |
| `SN` **required** |             |



## vehicle-info


### list

GET `/api/vehicle-info/`



**这里有几处跟Sandy的API不一样的地方：**

不提供 Availability 字段：因为跟status重复，（Status: 0:booked; 1=available; -1=deleted）

不提供 VehicleInfo字段：因其是 Manufacturer 和 Model 的拼接，没有必要也不应该，在此分别提供两个原始字段

不提供 Odo字段: 是 LastKnownOdo 和 LastOdo 字段的拼接，没有必要也不应该，在此分别提供两个原是字段

#### Search

**GET** `/api/vehicle-info?v_type=1,2&t_type=1,3`

| Parameter | Description         |
| :-------- | :------------------ |
| `v_type`  | VehicleTypeIDs      |
| `t_type`  | TransmissionTypeIDs |



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/vehicle-info/`



All Fields are **required** (所有字段必填)



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                  | Description |
| :------------------------- | :---------- |
| `Cdate`                    |             |
| `PlateNumber` **required** |             |
| `LastKnownOdo`             |             |
| `LastOdo`                  |             |
| `MFGDate`                  |             |
| `Manufacturer`             |             |
| `Model`                    |             |
| `Color`                    |             |
| `TransmissionTypeID`       |             |
| `VehicleTypeID`            |             |
| `AvailableKm`              |             |
| `DepartmentID`             |             |
| `FuelTypeID`               |             |
| `WoFExpDate`               |             |
| `RegoExpDate`              |             |
| `OriginalID`               |             |
| `Status`                   |             |



### due_list

GET `/api/vehicle-info/due/`



list all vehicles that with due WoF/Rego




### rego_due_list

GET `/api/vehicle-info/ergo-due/`



list vehicles that RegoExpired within 30 days




### wof_due_list

GET `/api/vehicle-info/wof-due/`



list vehicles that WofExpired within 30 days



### read

GET `/api/vehicle-info/{VehicleID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                | Description |
| :----------------------- | :---------- |
| `VehicleID` **required** |             |



### update

PUT `/api/vehicle-info/{VehicleID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                | Description |
| :----------------------- | :---------- |
| `VehicleID` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                  | Description |
| :------------------------- | :---------- |
| `Cdate`                    |             |
| `PlateNumber` **required** |             |
| `LastKnownOdo`             |             |
| `LastOdo`                  |             |
| `MFGDate`                  |             |
| `Manufacturer`             |             |
| `Model`                    |             |
| `Color`                    |             |
| `TransmissionTypeID`       |             |
| `VehicleTypeID`            |             |
| `AvailableKm`              |             |
| `DepartmentID`             |             |
| `FuelTypeID`               |             |
| `WoFExpDate`               |             |
| `RegoExpDate`              |             |
| `OriginalID`               |             |
| `Status`                   |             |



### partial_update

PATCH `/api/vehicle-info/{VehicleID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                | Description |
| :----------------------- | :---------- |
| `VehicleID` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter            | Description |
| :------------------- | :---------- |
| `Cdate`              |             |
| `PlateNumber`        |             |
| `LastKnownOdo`       |             |
| `LastOdo`            |             |
| `MFGDate`            |             |
| `Manufacturer`       |             |
| `Model`              |             |
| `Color`              |             |
| `TransmissionTypeID` |             |
| `VehicleTypeID`      |             |
| `AvailableKm`        |             |
| `DepartmentID`       |             |
| `FuelTypeID`         |             |
| `WoFExpDate`         |             |
| `RegoExpDate`        |             |
| `OriginalID`         |             |
| `Status`             |             |


### delete

DELETE `/api/vehicle-info/{VehicleID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                | Description |
| :----------------------- | :---------- |
| `VehicleID` **required** |             |



## workshop-info



### list

GET `/api/workshop-info/`



#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `page`      | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |



### create

POST `/api/workshop-info/`



All Fields are **required** except for **'SN'**



#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                   | Description |
| :-------------------------- | :---------- |
| `WorkshopName` **required** |             |
| `Address`                   |             |
| `ContactPerson`             |             |
| `ContactPhone`              |             |
| `Email`                     |             |
| `Note`                      |             |



### read

GET `/api/workshop-info/{WorkshopID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                 | Description |
| :------------------------ | :---------- |
| `WorkshopID` **required** |             |



### update

PUT `/api/workshop-info/{WorkshopID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                 | Description |
| :------------------------ | :---------- |
| `WorkshopID` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                   | Description |
| :-------------------------- | :---------- |
| `WorkshopName` **required** |             |
| `Address`                   |             |
| `ContactPerson`             |             |
| `ContactPhone`              |             |
| `Email`                     |             |
| `Note`                      |             |



### partial_update

PATCH `/api/workshop-info/{WorkshopID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                 | Description |
| :------------------------ | :---------- |
| `WorkshopID` **required** |             |

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter       | Description |
| :-------------- | :---------- |
| `WorkshopName`  |             |
| `Address`       |             |
| `ContactPerson` |             |
| `ContactPhone`  |             |
| `Email`         |             |
| `Note`          |             |



### delete

DELETE `/api/workshop-info/{WorkshopID}/`



#### Path Parameters

The following parameters should be included in the URL path.

| Parameter                 | Description |
| :------------------------ | :---------- |
| `WorkshopID` **required** |             |