import mparticle
batch = mparticle.Batch()
batch.environment = 'development'

configuration = mparticle.Configuration()
configuration.api_key = 'APP_KEY'
configuration.api_secret = 'APP_SECRET'
configuration.debug = True #enable logging of HTTP traffic
api_instance = mparticle.EventsApi(configuration)

identities = mparticle.UserIdentities()
identities.customerid = '123456'
identities.email = 'user@example.com'
batch.user_identities = identities

device_info = mparticle.DeviceInformation()
# set any IDs that you have for this user
device_info.ios_advertising_id = '07d2ebaa-e956-407e-a1e6-f05f871bf4e2'
device_info.android_advertising_id = 'a26f9736-c262-47ea-988b-0b0504cee874'
batch.device_info = device_info

batch.user_attributes = {'Account type': 'trial', 'TrialEndDate':'2016-12-01'}

app_event = mparticle.AppEvent('Example', 'navigation')
app_event.timestamp_unixtime_ms = 1596486455000

product = mparticle.Product()
product.name = 'Example Product'
product.id = 'sample-sku'
product.price = 19.99

product_action = mparticle.ProductAction('purchase')
product_action.products = [product]
product_action.tax_amount = 1.50
product_action.total_amount = 21.49

commerce_event = mparticle.CommerceEvent(product_action)
commerce_event.timestamp_unixtime_ms = 1596486455000

session_start = mparticle.SessionStartEvent()
session_start.session_id = 12345678
session_start.timestamp_unixtime_ms = 1596486455000

session_end = mparticle.SessionEndEvent()
session_end.session_id = session_start.session_id # its mandatory that these match
session_end.session_duration_ms = 1000
session_end.timestamp_unixtime_ms = 1596486455000 + 1000

batch.events = [session_start, session_end, app_event, commerce_event]

try:
    api_instance.upload_events(batch)
    # you can also send multiple batches at a time to decrease the amount of network calls
    #api_instance.bulk_upload_events([batch, batch])
except mparticle.rest.ApiException as e:
    print("Exception while calling mParticle: %s\n" % e)
