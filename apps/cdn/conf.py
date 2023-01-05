import environ, os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)

AWS_ACCESS_KEY_ID=env('AWS_KEY')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = 'pakthani'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETETS = {
"CacheControl": "max-age=86499",
}

DEFAULT_FILE_STORAGE = "apps.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "apps.cdn.backends.StaticRootS3Boto3Storage"