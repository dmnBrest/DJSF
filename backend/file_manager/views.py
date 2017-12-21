import sys, os, base64, datetime, hashlib, hmac
import urllib.parse
import requests
import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

access_key = settings.AWS_ACCESS_KEY_ID
secret_key = settings.AWS_SECRET_ACCESS_KEY
bucket = 'djsf1'
region = 'us-east-1'
amz_algorithm = 'AWS4-HMAC-SHA256'
service = 's3'

@login_required
def index(request):

    prefix = 'test2/1/'

    # Create a date for headers and the credential string
    t = datetime.datetime.utcnow()
    amz_date = t.strftime('%Y%m%dT%H%M%SZ')
    logger.debug(amz_date)
    date_stamp = t.strftime('%Y%m%d')  # Date w/o time, used in credential scope
    logger.debug(date_stamp)
    expiration_date = (t + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    logger.debug(expiration_date)

    amz_credential = access_key + '/' + date_stamp + '/' + region + '/' + service + '/aws4_request';

    payload = """{"expiration": "%s",
    "conditions": [
         {"bucket": "%s"},
         ["starts-with", "$key", "%s"],
         {"acl": "public-read"},
         ["starts-with", "$Content-Type", ""],
         {"x-amz-credential": "%s"},
         {"x-amz-algorithm": "%s"},
         {"x-amz-date": "%s"},
         {"success_action_status": "200" }
    ]
}""" % (expiration_date, bucket, prefix, amz_credential, amz_algorithm, amz_date)
    logger.debug(payload)

    policy = base64.b64encode(payload.encode())

    # Blob kdate = sign(Blob.valueOf('AWS4'+secret),Blob.valueOf(dateStamp));
	# Blob kregionName = sign(kdate, Blob.valueOf(region));
	# Blob kserviceName = sign(kregionName, Blob.valueOf('s3'));
	# Blob ksigning = sign(kserviceName, Blob.valueOf('aws4_request'));

	# signature = EncodingUtil.convertToHex( sign(ksigning, Blob.valueOf(policy)) );


    # payload_hash = hashlib.sha256(request_parameters.encode('utf-8')).hexdigest()
    # canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
    # credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'
    # string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + '\n' + hashlib.sha256(
    #     canonical_request.encode('utf-8')).hexdigest()
    # signing_key = getSignatureKey(secret_key, date_stamp, region, service)
    # signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
    # authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature
    #

    signing_key = getSignatureKey(secret_key, date_stamp, region, service)

    signature = hmac.new(signing_key, policy, hashlib.sha256).hexdigest()

    s3 = {
        'bucket': bucket,
        'region': region,
        'prefix': prefix,
        'policy': policy,
        'amz_credential': amz_credential,
        'amz_date': amz_date,
        'expiration_date': expiration_date,
        'amz_algorithm': amz_algorithm,
        'signature': signature
    }

    return render(request, 'file_manager/manager.html', {
        's3': s3
    })

# Key derivation functions. See:
# http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning