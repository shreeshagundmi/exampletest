# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Create your models here.
class Crud_Users(models.Model):
    name = models.CharField(max_length=70)


class ApiCrudUsers(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'API_crud_users'


class Actions(models.Model):
    aid = models.CharField(primary_key=True, max_length=255)
    type = models.CharField(max_length=32)
    callback = models.CharField(max_length=255)
    parameters = models.TextField()
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'actions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authmap(models.Model):
    aid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    authname = models.CharField(unique=True, max_length=128)
    module = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'authmap'


class AwsAmazonFiles(models.Model):
    fid = models.IntegerField(primary_key=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    bucket = models.CharField(max_length=255, blank=True, null=True)
    entity_type = models.CharField(max_length=255, blank=True, null=True)
    entity_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aws_amazon_files'


class Batch(models.Model):
    bid = models.PositiveIntegerField(primary_key=True)
    token = models.CharField(max_length=64)
    timestamp = models.IntegerField()
    batch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch'


class Block(models.Model):
    bid = models.AutoField(primary_key=True)
    module = models.CharField(max_length=64)
    delta = models.CharField(max_length=32)
    theme = models.CharField(max_length=64)
    status = models.IntegerField()
    weight = models.IntegerField()
    region = models.CharField(max_length=64)
    custom = models.IntegerField()
    visibility = models.IntegerField()
    pages = models.TextField()
    title = models.CharField(max_length=255)
    cache = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block'
        unique_together = (('theme', 'module', 'delta'),)


class BlockCustom(models.Model):
    bid = models.AutoField(primary_key=True)
    body = models.TextField(blank=True, null=True)
    info = models.CharField(unique=True, max_length=128)
    format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_custom'


class BlockNodeType(models.Model):
    module = models.CharField(max_length=64)
    delta = models.CharField(max_length=32)
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'block_node_type'
        unique_together = (('module', 'delta', 'type'),)


class BlockRole(models.Model):
    module = models.CharField(max_length=64)
    delta = models.CharField(max_length=32)
    rid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'block_role'
        unique_together = (('module', 'delta', 'rid'),)


class BlockedIps(models.Model):
    iid = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'blocked_ips'


class Cache(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheAdminMenu(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_admin_menu'


class CacheBlock(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_block'


class CacheBootstrap(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_bootstrap'


class CacheField(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_field'


class CacheFilter(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_filter'


class CacheForm(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_form'


class CacheImage(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_image'


class CacheLibraries(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_libraries'


class CacheMenu(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_menu'


class CachePage(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_page'


class CachePath(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_path'


class CacheUpdate(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_update'


class CacheVariable(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_variable'


class CacheViews(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_views'


class CacheViewsData(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_views_data'


class CaptchaPoints(models.Model):
    form_id = models.CharField(primary_key=True, max_length=128)
    module = models.CharField(max_length=64, blank=True, null=True)
    captcha_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'captcha_points'


class CaptchaSessions(models.Model):
    csid = models.AutoField(primary_key=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    uid = models.IntegerField()
    sid = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.IntegerField()
    form_id = models.CharField(max_length=128)
    solution = models.CharField(max_length=128)
    status = models.IntegerField()
    attempts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'captcha_sessions'


class Certificates(models.Model):
    ctid = models.AutoField(primary_key=True)
    cert_name = models.CharField(max_length=255)
    cert_image = models.IntegerField()
    is_default = models.IntegerField()
    created_on = models.IntegerField()
    created_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'certificates'


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    nid = models.IntegerField()
    uid = models.IntegerField()
    subject = models.CharField(max_length=64)
    hostname = models.CharField(max_length=128)
    created = models.IntegerField()
    changed = models.IntegerField()
    status = models.PositiveIntegerField()
    thread = models.CharField(max_length=255)
    name = models.CharField(max_length=60, blank=True, null=True)
    mail = models.CharField(max_length=64, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'comment'


class CrudCrudUsers(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'crud_crud_users'


class CtoolsCssCache(models.Model):
    cid = models.CharField(primary_key=True, max_length=128)
    filename = models.CharField(max_length=255, blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    filter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctools_css_cache'


class CtoolsObjectCache(models.Model):
    sid = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    obj = models.CharField(max_length=32)
    updated = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctools_object_cache'
        unique_together = (('sid', 'obj', 'name'),)


class DateFormatLocale(models.Model):
    format = models.CharField(max_length=100)
    type = models.CharField(max_length=64)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'date_format_locale'
        unique_together = (('type', 'language'),)


class DateFormatType(models.Model):
    type = models.CharField(primary_key=True, max_length=64)
    title = models.CharField(max_length=255)
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'date_format_type'


class DateFormats(models.Model):
    dfid = models.AutoField(primary_key=True)
    format = models.CharField(max_length=100)
    type = models.CharField(max_length=64)
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'date_formats'
        unique_together = (('format', 'type'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailReminder(models.Model):
    erid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    event = models.CharField(max_length=255, blank=True, null=True)
    email_index = models.PositiveIntegerField(blank=True, null=True)
    sent_date = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_reminder'


class FieldConfig(models.Model):
    field_name = models.CharField(max_length=32)
    type = models.CharField(max_length=128)
    module = models.CharField(max_length=128)
    active = models.IntegerField()
    storage_type = models.CharField(max_length=128)
    storage_module = models.CharField(max_length=128)
    storage_active = models.IntegerField()
    locked = models.IntegerField()
    data = models.TextField()
    cardinality = models.IntegerField()
    translatable = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'field_config'


class FieldConfigInstance(models.Model):
    field_id = models.IntegerField()
    field_name = models.CharField(max_length=32)
    entity_type = models.CharField(max_length=32)
    bundle = models.CharField(max_length=128)
    data = models.TextField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'field_config_instance'


class FieldDataBody(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    body_value = models.TextField(blank=True, null=True)
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_data_body'
        unique_together = (('entity_type', 'entity_id', 'deleted', 'delta', 'language'),)


class FieldDataCommentBody(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    comment_body_value = models.TextField(blank=True, null=True)
    comment_body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_data_comment_body'
        unique_together = (('entity_type', 'entity_id', 'deleted', 'delta', 'language'),)


class FieldDataFieldImage(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    field_image_fid = models.PositiveIntegerField(blank=True, null=True)
    field_image_alt = models.CharField(max_length=512, blank=True, null=True)
    field_image_title = models.CharField(max_length=1024, blank=True, null=True)
    field_image_width = models.PositiveIntegerField(blank=True, null=True)
    field_image_height = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_data_field_image'
        unique_together = (('entity_type', 'entity_id', 'deleted', 'delta', 'language'),)


class FieldDataFieldTags(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    field_tags_tid = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_data_field_tags'
        unique_together = (('entity_type', 'entity_id', 'deleted', 'delta', 'language'),)


class FieldRevisionBody(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField()
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    body_value = models.TextField(blank=True, null=True)
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_revision_body'
        unique_together = (('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language'),)


class FieldRevisionCommentBody(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField()
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    comment_body_value = models.TextField(blank=True, null=True)
    comment_body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_revision_comment_body'
        unique_together = (('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language'),)


class FieldRevisionFieldImage(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField()
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    field_image_fid = models.PositiveIntegerField(blank=True, null=True)
    field_image_alt = models.CharField(max_length=512, blank=True, null=True)
    field_image_title = models.CharField(max_length=1024, blank=True, null=True)
    field_image_width = models.PositiveIntegerField(blank=True, null=True)
    field_image_height = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_revision_field_image'
        unique_together = (('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language'),)


class FieldRevisionFieldTags(models.Model):
    entity_type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField()
    language = models.CharField(max_length=32)
    delta = models.PositiveIntegerField()
    field_tags_tid = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_revision_field_tags'
        unique_together = (('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language'),)


class FileManaged(models.Model):
    fid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    filename = models.CharField(max_length=255)
    uri = models.CharField(unique=True, max_length=255)
    filemime = models.CharField(max_length=255)
    filesize = models.PositiveBigIntegerField()
    status = models.IntegerField()
    timestamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'file_managed'


class FileUsage(models.Model):
    fid = models.PositiveIntegerField(primary_key=True)
    module = models.CharField(max_length=255)
    type = models.CharField(max_length=64)
    id = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'file_usage'
        unique_together = (('fid', 'type', 'id', 'module'),)


class Filter(models.Model):
    format = models.CharField(max_length=255)
    module = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    weight = models.IntegerField()
    status = models.IntegerField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter'
        unique_together = (('format', 'name'),)


class FilterFormat(models.Model):
    format = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(unique=True, max_length=255)
    cache = models.IntegerField()
    status = models.PositiveIntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter_format'


class Flood(models.Model):
    fid = models.AutoField(primary_key=True)
    event = models.CharField(max_length=64)
    identifier = models.CharField(max_length=128)
    timestamp = models.IntegerField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'flood'


class FormBuilderCache(models.Model):
    sid = models.CharField(max_length=64, blank=True, null=True)
    form_id = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    updated = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_builder_cache'


class HelpInfo(models.Model):
    hid = models.AutoField(primary_key=True)
    help_menu = models.CharField(max_length=255, blank=True, null=True)
    help_text = models.TextField(blank=True, null=True)
    help_status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help_info'


class History(models.Model):
    uid = models.IntegerField()
    nid = models.PositiveIntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history'
        unique_together = (('uid', 'nid'),)


class I18NString(models.Model):
    lid = models.IntegerField(primary_key=True)
    textgroup = models.CharField(max_length=50)
    context = models.CharField(max_length=255)
    objectid = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    property = models.CharField(max_length=255)
    objectindex = models.IntegerField()
    format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i18n_string'


class ImageEffects(models.Model):
    ieid = models.AutoField(primary_key=True)
    isid = models.PositiveIntegerField()
    weight = models.IntegerField()
    name = models.CharField(max_length=255)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'image_effects'


class ImageStyles(models.Model):
    isid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'image_styles'


class InfoReportsData10(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_photo4_id = models.IntegerField(blank=True, null=True)
    ques_photo_4 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_10'


class InfoReportsData11(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo2_id = models.IntegerField(blank=True, null=True)
    ques_photo_2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_11'


class InfoReportsData110(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_email_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_textfield_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_6 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_7_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_7_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_7_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_7_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_7_5 = models.IntegerField(blank=True, null=True)
    ques_photo8_id = models.IntegerField(blank=True, null=True)
    ques_photo_8 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_110'


class InfoReportsData115(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_5 = models.IntegerField(blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_115'


class InfoReportsData116(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_5 = models.IntegerField(blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_116'


class InfoReportsData118(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_118'


class InfoReportsData119(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_1 = models.BigIntegerField(blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_119'


class InfoReportsData120(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_120'


class InfoReportsData122(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_122'


class InfoReportsData123(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_6 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_123'


class InfoReportsData124(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_5 = models.IntegerField(blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_124'


class InfoReportsData125(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_125'


class InfoReportsData126(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_126'


class InfoReportsData145(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_145'


class InfoReportsData15(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_15'


class InfoReportsData16(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_number_2 = models.BigIntegerField(blank=True, null=True)
    ques_email_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo4_id = models.IntegerField(blank=True, null=True)
    ques_photo_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_16'


class InfoReportsData164(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_164'


class InfoReportsData165(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_165'


class InfoReportsData166(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_166'


class InfoReportsData167(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_167'


class InfoReportsData169(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_169'


class InfoReportsData171(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_171'


class InfoReportsData172(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_172'


class InfoReportsData173(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_5 = models.IntegerField(blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_173'


class InfoReportsData174(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_174'


class InfoReportsData175(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_175'


class InfoReportsData176(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_176'


class InfoReportsData177(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_number_1 = models.BigIntegerField(blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_177'


class InfoReportsData178(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_1_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_1_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_1_3 = models.IntegerField(blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_178'


class InfoReportsData179(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_179'


class InfoReportsData18(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_18'


class InfoReportsData184(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_5 = models.IntegerField(blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_184'


class InfoReportsData2(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_2'


class InfoReportsData20(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_20'


class InfoReportsData204(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_204'


class InfoReportsData205(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_205'


class InfoReportsData21(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_21'


class InfoReportsData212(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_212'


class InfoReportsData217(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_217'


class InfoReportsData218(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textarea_2 = models.TextField(blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_218'


class InfoReportsData22(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_22'


class InfoReportsData220(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_7 = models.CharField(max_length=255, blank=True, null=True)
    ques_textarea_3 = models.TextField(blank=True, null=True)
    ques_date_11 = models.IntegerField(blank=True, null=True)
    ques_time_12 = models.IntegerField(blank=True, null=True)
    ques_email_9 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_4 = models.IntegerField(blank=True, null=True)
    ques_select6_id = models.IntegerField(blank=True, null=True)
    ques_select_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo10_id = models.IntegerField(blank=True, null=True)
    ques_photo_10 = models.CharField(max_length=255, blank=True, null=True)
    ques_voice13_id = models.IntegerField(blank=True, null=True)
    ques_voice_13 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_220'


class InfoReportsData223(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_textarea_4 = models.TextField(blank=True, null=True)
    ques_textfield_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_email_12 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo14_id = models.IntegerField(blank=True, null=True)
    ques_photo_14 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_7 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_8_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_8_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_8_3 = models.IntegerField(blank=True, null=True)
    ques_select9_id = models.IntegerField(blank=True, null=True)
    ques_select_9 = models.CharField(max_length=255, blank=True, null=True)
    ques_time_11 = models.IntegerField(blank=True, null=True)
    ques_date_10 = models.IntegerField(blank=True, null=True)
    ques_voice15_id = models.IntegerField(blank=True, null=True)
    ques_voice_15 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_223'


class InfoReportsData228(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_textarea_4 = models.TextField(blank=True, null=True)
    ques_email_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_date_7 = models.IntegerField(blank=True, null=True)
    ques_time_8 = models.IntegerField(blank=True, null=True)
    ques_multiple_9_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_9_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_9_3 = models.IntegerField(blank=True, null=True)
    ques_photo10_id = models.IntegerField(blank=True, null=True)
    ques_photo_10 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo11_id = models.IntegerField(blank=True, null=True)
    ques_photo_11 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_228'


class InfoReportsData23(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_23'


class InfoReportsData236(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_select7_id = models.IntegerField(blank=True, null=True)
    ques_select_7 = models.CharField(max_length=255, blank=True, null=True)
    ques_date_6 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_236'


class InfoReportsData238(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_238'


class InfoReportsData239(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_date_4 = models.IntegerField(blank=True, null=True)
    ques_photo7_id = models.IntegerField(blank=True, null=True)
    ques_photo_7 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_8_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_8_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_8_3 = models.IntegerField(blank=True, null=True)
    ques_email_9 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_239'


class InfoReportsData24(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_number_1 = models.BigIntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_24'


class InfoReportsData240(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_email_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_voice8_id = models.IntegerField(blank=True, null=True)
    ques_voice_8 = models.CharField(max_length=255, blank=True, null=True)
    ques_select9_id = models.IntegerField(blank=True, null=True)
    ques_select_9 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_240'


class InfoReportsData241(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_4 = models.BigIntegerField(blank=True, null=True)
    ques_select6_id = models.IntegerField(blank=True, null=True)
    ques_select_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_date_7 = models.IntegerField(blank=True, null=True)
    ques_email_9 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo10_id = models.IntegerField(blank=True, null=True)
    ques_photo_10 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo12_id = models.IntegerField(blank=True, null=True)
    ques_photo_12 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_241'


class InfoReportsData242(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_5 = models.BigIntegerField(blank=True, null=True)
    ques_email_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo7_id = models.IntegerField(blank=True, null=True)
    ques_photo_7 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo10_id = models.IntegerField(blank=True, null=True)
    ques_photo_10 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_242'


class InfoReportsData25(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_2 = models.BigIntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_25'


class InfoReportsData250(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_email_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_voice8_id = models.IntegerField(blank=True, null=True)
    ques_voice_8 = models.CharField(max_length=255, blank=True, null=True)
    ques_select9_id = models.IntegerField(blank=True, null=True)
    ques_select_9 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_250'


class InfoReportsData255(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_6_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_6_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_6_3 = models.IntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_255'


class InfoReportsData258(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_select4_id = models.IntegerField(blank=True, null=True)
    ques_select_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_3 = models.IntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_258'


class InfoReportsData259(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_select4_id = models.IntegerField(blank=True, null=True)
    ques_select_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_3 = models.IntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_259'


class InfoReportsData26(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_2 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_3_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_3 = models.IntegerField(blank=True, null=True)
    ques_photo4_id = models.IntegerField(blank=True, null=True)
    ques_photo_4 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_26'


class InfoReportsData260(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_select4_id = models.IntegerField(blank=True, null=True)
    ques_select_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_5_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_5_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_3_3 = models.IntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_260'


class InfoReportsData261(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_select5_id = models.IntegerField(blank=True, null=True)
    ques_select_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_voice7_id = models.IntegerField(blank=True, null=True)
    ques_voice_7 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_261'


class InfoReportsData262(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_select5_id = models.IntegerField(blank=True, null=True)
    ques_select_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_voice7_id = models.IntegerField(blank=True, null=True)
    ques_voice_7 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo8_id = models.IntegerField(blank=True, null=True)
    ques_photo_8 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_262'


class InfoReportsData263(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_263'


class InfoReportsData264(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_date_4 = models.IntegerField(blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_email_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_264'


class InfoReportsData27(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_27'


class InfoReportsData271(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_email_4 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_271'


class InfoReportsData273(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_3 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_273'


class InfoReportsData275(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo4_id = models.IntegerField(blank=True, null=True)
    ques_photo_4 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_275'


class InfoReportsData278(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_date_7 = models.IntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_278'


class InfoReportsData28(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_28'


class InfoReportsData280(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_280'


class InfoReportsData281(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_voice2_id = models.IntegerField(blank=True, null=True)
    ques_voice_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo3_id = models.IntegerField(blank=True, null=True)
    ques_photo_3 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_281'


class InfoReportsData287(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_email_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_barcode_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_video4_id = models.IntegerField(blank=True, null=True)
    ques_video_4 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_287'


class InfoReportsData289(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_select1_id = models.IntegerField(blank=True, null=True)
    ques_select_1 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_289'


class InfoReportsData29(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo3_id = models.IntegerField(blank=True, null=True)
    ques_photo_3 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_29'


class InfoReportsData299(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    ques_textarea_4 = models.TextField(blank=True, null=True)
    ques_number_5 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_6_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_6_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_6_3 = models.IntegerField(blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    barcode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_299'


class InfoReportsData3(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_photo7_id = models.IntegerField(blank=True, null=True)
    ques_photo_7 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_date_6 = models.IntegerField(blank=True, null=True)
    ques_select5_id = models.IntegerField(blank=True, null=True)
    ques_select_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_video9_id = models.IntegerField(blank=True, null=True)
    ques_video_9 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    barcode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_3'


class InfoReportsData30(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_30'


class InfoReportsData300(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_textarea_3 = models.TextField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_300'


class InfoReportsData32(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_2 = models.BigIntegerField(blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_32'


class InfoReportsData33(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_date_3 = models.IntegerField(blank=True, null=True)
    ques_photo4_id = models.IntegerField(blank=True, null=True)
    ques_photo_4 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_33'


class InfoReportsData34(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_34'


class InfoReportsData38(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo6_id = models.IntegerField(blank=True, null=True)
    ques_photo_6 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_38'


class InfoReportsData39(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_6 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_39'


class InfoReportsData40(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_number_6 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_40'


class InfoReportsData42(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_42'


class InfoReportsData43(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo3_id = models.IntegerField(blank=True, null=True)
    ques_photo_3 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_43'


class InfoReportsData44(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_44'


class InfoReportsData46(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_46'


class InfoReportsData48(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_48'


class InfoReportsData49(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_photo7_id = models.IntegerField(blank=True, null=True)
    ques_photo_7 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_49'


class InfoReportsData50(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_50'


class InfoReportsData59(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_6 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_59'


class InfoReportsData61(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_6 = models.BigIntegerField(blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_61'


class InfoReportsData63(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    acid = models.PositiveIntegerField()
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_contact_no = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.CharField(max_length=255, blank=True, null=True)
    account_city = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.CharField(max_length=255, blank=True, null=True)
    account_country = models.CharField(max_length=255, blank=True, null=True)
    acc_zone = models.CharField(max_length=255, blank=True, null=True)
    acc_department = models.CharField(max_length=255, blank=True, null=True)
    acc_zone1 = models.CharField(max_length=255, blank=True, null=True)
    acc_region = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_1 = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_3 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    discount = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_63'


class InfoReportsData67(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_67'


class InfoReportsData69(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_69'


class InfoReportsData85(models.Model):
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    submission_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_mobile = models.CharField(max_length=255, blank=True, null=True)
    user_region = models.CharField(max_length=255, blank=True, null=True)
    user_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    user_department = models.CharField(max_length=255, blank=True, null=True)
    user_regini = models.CharField(max_length=255, blank=True, null=True)
    user_region1 = models.CharField(max_length=255, blank=True, null=True)
    user_manager_name = models.CharField(max_length=255, blank=True, null=True)
    ques_textfield_2 = models.CharField(max_length=255, blank=True, null=True)
    ques_number_3 = models.BigIntegerField(blank=True, null=True)
    ques_multiple_4_1 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_2 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_3 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_4 = models.IntegerField(blank=True, null=True)
    ques_multiple_4_5 = models.IntegerField(blank=True, null=True)
    ques_photo5_id = models.IntegerField(blank=True, null=True)
    ques_photo_5 = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()
    revenue = models.FloatField()
    final_revenue = models.FloatField()
    code_product_type = models.CharField(max_length=255, blank=True, null=True)
    code_gst_price = models.IntegerField(blank=True, null=True)
    code_mrp = models.CharField(max_length=255, blank=True, null=True)
    code_fixed_price = models.IntegerField(blank=True, null=True)
    code_cgst = models.IntegerField(blank=True, null=True)
    code_mrp1 = models.CharField(max_length=255, blank=True, null=True)
    code_mrp2 = models.CharField(max_length=255, blank=True, null=True)
    ymd = models.PositiveIntegerField(blank=True, null=True)
    ym = models.PositiveIntegerField(blank=True, null=True)
    yw = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    user_shree_attr = models.CharField(max_length=255, blank=True, null=True)
    user_jaison = models.CharField(max_length=255, blank=True, null=True)
    user_werkhk = models.CharField(max_length=255, blank=True, null=True)
    code_new_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_reports_data_85'


class InfogeonAccounts(models.Model):
    acid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    guid = models.CharField(max_length=255)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    master_account_name = models.CharField(max_length=200, blank=True, null=True)
    account_manager_id = models.PositiveIntegerField()
    website = models.CharField(max_length=100, blank=True, null=True)
    account_logo = models.PositiveIntegerField()
    account_fburl = models.CharField(max_length=100, blank=True, null=True)
    account_linkedurl = models.CharField(max_length=100, blank=True, null=True)
    account_twitterurl = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_accounts'


class InfogeonAddress(models.Model):
    aid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    name = models.CharField(max_length=256)
    entity_type = models.CharField(max_length=10, blank=True, null=True)
    entity_id = models.IntegerField()
    address_type = models.PositiveIntegerField(blank=True, null=True)
    street = models.CharField(max_length=256, blank=True, null=True)
    locality = models.CharField(max_length=256, blank=True, null=True)
    landmark = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.PositiveIntegerField(blank=True, null=True)
    country = models.PositiveIntegerField(blank=True, null=True)
    pin = models.PositiveIntegerField()
    is_deleted = models.IntegerField(blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    lat_lng = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_address'


class InfogeonAttributeOptions(models.Model):
    aoid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    aid = models.PositiveIntegerField()
    attribute_option = models.CharField(max_length=255, blank=True, null=True)
    attribute_desc = models.CharField(max_length=255, blank=True, null=True)
    group_admin = models.PositiveIntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_attribute_options'


class InfogeonAttributes(models.Model):
    aid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    attribute_name = models.CharField(max_length=255, blank=True, null=True)
    attribute_desc = models.CharField(max_length=255, blank=True, null=True)
    is_group = models.PositiveIntegerField(blank=True, null=True)
    is_options = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_attributes'


class InfogeonAwsNotification(models.Model):
    awsnid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    type = models.CharField(max_length=50)
    category1 = models.CharField(max_length=255)
    category2_id = models.CharField(max_length=255)
    category2_type = models.CharField(max_length=50)
    category2_value = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    msg = models.TextField()
    aws_status = models.CharField(max_length=50)
    created_on = models.IntegerField()
    updated_on = models.IntegerField()
    created_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_aws_notification'


class InfogeonBsharpInsightsKey(models.Model):
    api_key = models.CharField(max_length=255)
    auth_token = models.CharField(max_length=255)
    domain_name = models.CharField(max_length=255)
    created_on = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_bsharp_insights_key'


class InfogeonBsharpInsightsUserData(models.Model):
    cmid = models.IntegerField()
    uid = models.IntegerField()
    zuid = models.CharField(max_length=25)
    token = models.CharField(max_length=255)
    redirect_url = models.CharField(max_length=300)
    created_on = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_bsharp_insights_user_data'


class InfogeonCertificateTemplates(models.Model):
    ictid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    cert_title = models.CharField(max_length=255)
    cert_type = models.CharField(max_length=50)
    is_default = models.IntegerField()
    certificate_image = models.IntegerField()
    created_on = models.IntegerField()
    updated_on = models.IntegerField()
    created_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_certificate_templates'


class InfogeonChannelManagers(models.Model):
    cmgrid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    chid = models.IntegerField()
    uid = models.IntegerField()
    assigned_on = models.IntegerField()
    assigned_by = models.IntegerField()
    updated_on = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_channel_managers'


class InfogeonChannels(models.Model):
    chid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    channel_name = models.CharField(max_length=255, blank=True, null=True)
    channel_desc = models.CharField(max_length=255, blank=True, null=True)
    channel_tags = models.TextField(blank=True, null=True)
    channel_image = models.PositiveIntegerField()
    channel_weight = models.IntegerField()
    channel_manager = models.IntegerField()
    featured = models.IntegerField()
    created_on = models.IntegerField(blank=True, null=True)
    updated_on = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_channels'


class InfogeonChannelsModule(models.Model):
    chmid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    chid = models.IntegerField()
    mid = models.IntegerField()
    weight = models.IntegerField()
    assigned_on = models.IntegerField()
    updated_on = models.IntegerField()
    assigned_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_channels_module'


class InfogeonCompanies(models.Model):
    cmid = models.AutoField(primary_key=True)
    cm_name = models.CharField(max_length=255, blank=True, null=True)
    cm_desc = models.CharField(max_length=255, blank=True, null=True)
    logo_image_fid = models.IntegerField()
    home_image = models.IntegerField()
    created_on = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_companies'


class InfogeonDocumentMatrix(models.Model):
    dmid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    guid = models.CharField(max_length=255)
    mid = models.IntegerField()
    uid = models.IntegerField()
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    time_spent = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    user_attempts = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    week = models.IntegerField()
    capture_date = models.IntegerField()
    created_time = models.IntegerField()
    device_type = models.IntegerField()
    viewed = models.IntegerField()
    device_info = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_document_matrix'


class InfogeonDocuments(models.Model):
    docid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    doc_name = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=50)
    doc_image = models.PositiveIntegerField()
    doc_desc = models.CharField(max_length=255)
    doc_tags = models.CharField(max_length=255)
    doc_link = models.CharField(max_length=255)
    doc_file = models.PositiveIntegerField()
    created_on = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_on = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_documents'


class InfogeonEntityAttributeOptions(models.Model):
    eaoid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    eaid = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    attribute_option = models.CharField(max_length=255, blank=True, null=True)
    attribute_desc = models.CharField(max_length=255, blank=True, null=True)
    group_admin = models.PositiveIntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_entity_attribute_options'


class InfogeonEntityAttributeValues(models.Model):
    eavid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    entity_id = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    eaid = models.PositiveIntegerField()
    eaoid = models.PositiveIntegerField()
    attribute_value = models.CharField(max_length=100, blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_entity_attribute_values'


class InfogeonEntityAttributes(models.Model):
    eaid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    attribute_name = models.CharField(max_length=255, blank=True, null=True)
    attribute_desc = models.CharField(max_length=255, blank=True, null=True)
    is_group = models.PositiveIntegerField(blank=True, null=True)
    is_options = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    created_date = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_entity_attributes'


class InfogeonEntityCustomerAttributes(models.Model):
    ecaid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    entity_id = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    eaid = models.PositiveIntegerField()
    eaoid = models.PositiveIntegerField()
    attribute_value = models.CharField(max_length=100, blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_entity_customer_attributes'


class InfogeonEntityCustomerGroups(models.Model):
    ecgid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    entity_id = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    egid = models.PositiveIntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_entity_customer_groups'


class InfogeonEntityGroups(models.Model):
    egid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    group_type = models.CharField(max_length=120, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    group_desc = models.CharField(max_length=255, blank=True, null=True)
    group_admin = models.PositiveIntegerField()
    is_flex_group = models.PositiveIntegerField(blank=True, null=True)
    eaoid = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    created_date = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_entity_groups'


class InfogeonGroups(models.Model):
    gid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    group_type = models.CharField(max_length=120, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    group_desc = models.CharField(max_length=255, blank=True, null=True)
    group_admin = models.PositiveIntegerField()
    is_flex_group = models.PositiveIntegerField(blank=True, null=True)
    aoid = models.PositiveIntegerField()
    created_date = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_groups'


class InfogeonInfocaptureCodeFormDetails(models.Model):
    cfdid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    code_name = models.IntegerField()
    volume = models.FloatField()
    revenue = models.IntegerField()
    discount = models.FloatField()
    comment = models.IntegerField()
    barcode = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_code_form_details'


class InfogeonInfocaptureCodeResponse(models.Model):
    crid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    code_name = models.CharField(max_length=255, blank=True, null=True)
    volume = models.IntegerField()
    revenue = models.FloatField()
    discount = models.IntegerField()
    final_revenue = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    barcode = models.CharField(max_length=255)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_code_response'


class InfogeonInfocaptureCodes(models.Model):
    cdid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    code_name = models.CharField(max_length=255)
    gid = models.CharField(max_length=50)
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_codes'


class InfogeonInfocaptureDuedate(models.Model):
    rdid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    duedate = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_duedate'


class InfogeonInfocaptureDuedateSubmission(models.Model):
    rdsid = models.AutoField(primary_key=True)
    sid = models.PositiveIntegerField()
    cmid = models.PositiveIntegerField()
    rdid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    user_submited_date = models.PositiveIntegerField(blank=True, null=True)
    server_uploaded_date = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_duedate_submission'


class InfogeonInfocaptureGroupsNode(models.Model):
    gnid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    gid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_groups_node'


class InfogeonInfocaptureLatlong(models.Model):
    ltid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    guid = models.CharField(max_length=255, blank=True, null=True)
    sid = models.PositiveIntegerField()
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.PositiveIntegerField(blank=True, null=True)
    entity_id = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_latlong'


class InfogeonInfocapturePoints(models.Model):
    ptsid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    cid = models.PositiveIntegerField()
    type = models.CharField(max_length=16, blank=True, null=True)
    option_id = models.CharField(max_length=128)
    rules_id = models.PositiveIntegerField()
    rules_operator = models.CharField(max_length=128)
    rules_info = models.CharField(max_length=250)
    range_from = models.CharField(max_length=250)
    range_to = models.CharField(max_length=250)
    points = models.CharField(max_length=100)
    created_date = models.IntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_points'


class InfogeonInfocapturePointsDetails(models.Model):
    ptsdid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    cid = models.PositiveIntegerField()
    type = models.CharField(max_length=30)
    option_id = models.CharField(max_length=128)
    points = models.CharField(max_length=150)
    capture_date = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_points_details'


class InfogeonInfocaptureRecurrence(models.Model):
    rid = models.AutoField(primary_key=True)
    nid = models.PositiveIntegerField()
    cmid = models.PositiveIntegerField()
    gid = models.CharField(max_length=150)
    occurrence_type = models.PositiveIntegerField()
    gps = models.PositiveIntegerField()
    details = models.CharField(max_length=20, blank=True, null=True)
    periodic_type = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    duedate_type = models.PositiveIntegerField(blank=True, null=True)
    duedate_details = models.PositiveIntegerField(blank=True, null=True)
    is_customer_form = models.PositiveIntegerField()
    template_id = models.IntegerField()
    is_points = models.FloatField()
    info_rules = models.TextField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_infocapture_recurrence'


class InfogeonLeadActionItems(models.Model):
    lead_act_id = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    lead_guid = models.CharField(max_length=200, blank=True, null=True)
    lead_act_name = models.CharField(max_length=200, blank=True, null=True)
    lead_act_text = models.CharField(max_length=255, blank=True, null=True)
    lead_act_type = models.IntegerField()
    lead_act_setvalue = models.IntegerField()
    lead_act_created = models.PositiveIntegerField(blank=True, null=True)
    lead_act_updated = models.PositiveIntegerField(blank=True, null=True)
    lead_act_assigned = models.PositiveIntegerField(blank=True, null=True)
    lead_act_createdby = models.PositiveIntegerField(blank=True, null=True)
    lead_act_status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_lead_action_items'


class InfogeonLeadChild(models.Model):
    lead_cid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    lead_mid = models.PositiveIntegerField()
    lead_c_name = models.CharField(max_length=200, blank=True, null=True)
    lead_c_mobile = models.CharField(max_length=20, blank=True, null=True)
    lead_c_email_id = models.CharField(max_length=100, blank=True, null=True)
    lead_c_city = models.CharField(max_length=150, blank=True, null=True)
    lead_c_pin = models.IntegerField(blank=True, null=True)
    lead_c_lat = models.CharField(max_length=20, blank=True, null=True)
    lead_c_lng = models.CharField(max_length=20, blank=True, null=True)
    lead_c_notes = models.CharField(max_length=255, blank=True, null=True)
    lead_c_created_on = models.PositiveIntegerField(blank=True, null=True)
    lead_c_updated_on = models.PositiveIntegerField(blank=True, null=True)
    lead_c_created_by = models.PositiveIntegerField(blank=True, null=True)
    lead_c_assigned_uid = models.PositiveIntegerField(blank=True, null=True)
    lead_c_assigned_account = models.CharField(max_length=255, blank=True, null=True)
    lead_c_assigned_type = models.PositiveIntegerField(blank=True, null=True)
    lead_c_stage = models.PositiveIntegerField(blank=True, null=True)
    lead_c_product = models.PositiveIntegerField(blank=True, null=True)
    lead_c_program = models.PositiveIntegerField(blank=True, null=True)
    lead_c_source = models.PositiveIntegerField(blank=True, null=True)
    lead_c_status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_lead_child'


class InfogeonLeadConfiguration(models.Model):
    lead_configid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    lead_config_name = models.CharField(max_length=200, blank=True, null=True)
    lead_config_desc = models.CharField(max_length=255, blank=True, null=True)
    lead_config_type = models.IntegerField()
    lead_config_weight = models.IntegerField()
    lead_default_type = models.IntegerField()
    lead_config_created_on = models.PositiveIntegerField(blank=True, null=True)
    lead_config_updated_on = models.PositiveIntegerField(blank=True, null=True)
    lead_config_created_by = models.PositiveIntegerField(blank=True, null=True)
    lead_config_status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_lead_configuration'


class InfogeonLeadMaster(models.Model):
    lead_mid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    lead_m_name = models.CharField(max_length=200, blank=True, null=True)
    lead_m_mobile = models.CharField(max_length=20, blank=True, null=True)
    lead_m_email_id = models.CharField(max_length=100, blank=True, null=True)
    lead_m_city = models.CharField(max_length=150, blank=True, null=True)
    lead_m_pin = models.IntegerField(blank=True, null=True)
    lead_m_lat = models.CharField(max_length=20, blank=True, null=True)
    lead_m_lng = models.CharField(max_length=20, blank=True, null=True)
    lead_m_guid = models.CharField(max_length=255, blank=True, null=True)
    lead_m_closure = models.PositiveIntegerField(blank=True, null=True)
    lead_m_notes = models.CharField(max_length=255, blank=True, null=True)
    lead_m_created_on = models.PositiveIntegerField(blank=True, null=True)
    lead_m_updated_on = models.PositiveIntegerField(blank=True, null=True)
    lead_m_created_by = models.PositiveIntegerField(blank=True, null=True)
    lead_m_stage = models.PositiveIntegerField(blank=True, null=True)
    lead_m_product = models.PositiveIntegerField(blank=True, null=True)
    lead_m_program = models.PositiveIntegerField(blank=True, null=True)
    lead_m_source = models.PositiveIntegerField(blank=True, null=True)
    lead_m_status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_lead_master'


class InfogeonModuleCertificates(models.Model):
    mctid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    ictid = models.IntegerField()
    assigned_on = models.IntegerField()
    updated_on = models.IntegerField()
    assigned_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_module_certificates'


class InfogeonModuleFeedback(models.Model):
    mfid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    guid = models.CharField(max_length=255)
    uid = models.IntegerField()
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    feedback = models.CharField(max_length=255)
    rating = models.FloatField()
    feedback_date = models.IntegerField()
    created_time = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_module_feedback'


class InfogeonModuleUsers(models.Model):
    muid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    mid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    gid = models.IntegerField()
    pass_status = models.CharField(max_length=50, blank=True, null=True)
    user_points = models.CharField(max_length=150)
    completed_date = models.IntegerField()
    group_type = models.IntegerField()
    assigned_on = models.IntegerField()
    updated_on = models.IntegerField()
    assigned_by = models.IntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_module_users'


class InfogeonModuleUsersInfo(models.Model):
    muiid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    uid = models.IntegerField()
    pass_status = models.CharField(max_length=150)
    user_points = models.CharField(max_length=150)
    completed_date = models.IntegerField()
    user_assigned_on = models.IntegerField()
    updated_on = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_module_users_info'


class InfogeonModules(models.Model):
    mid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    module_name = models.CharField(max_length=255)
    module_desc = models.CharField(max_length=255)
    module_tags = models.CharField(max_length=255)
    module_image = models.IntegerField()
    created_on = models.IntegerField()
    end_date = models.IntegerField()
    featured = models.IntegerField()
    updated_on = models.PositiveIntegerField()
    created_by = models.IntegerField()
    firebase_id = models.CharField(max_length=150)
    chat_name = models.CharField(max_length=255)
    chat_status = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_modules'


class InfogeonModulesDocuments(models.Model):
    mdid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    md_doc_name = models.CharField(max_length=255)
    md_doc_tags = models.CharField(max_length=255)
    md_doc_desc = models.TextField()
    md_weight = models.IntegerField()
    end_date = models.IntegerField()
    time_limit_min = models.IntegerField()
    time_limit_sec = models.IntegerField()
    is_pass = models.IntegerField()
    min_pass_score = models.FloatField()
    assigned_on = models.IntegerField()
    assigned_by = models.IntegerField()
    updated_on = models.IntegerField()
    deleted_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_modules_documents'


class InfogeonModulesNotification(models.Model):
    mnid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    new_doc = models.IntegerField(blank=True, null=True)
    user_reminder = models.IntegerField()
    admin_reminder = models.IntegerField()
    consumption_status = models.IntegerField()
    mgr_consumption_status = models.IntegerField()
    module_feedback = models.IntegerField()
    doc_feedback = models.IntegerField()
    pass_all_docs_viewed = models.IntegerField()
    all_docs_viewed_points = models.CharField(max_length=50)
    quiz_avg_pass_percent = models.CharField(max_length=50)
    created_on = models.IntegerField()
    updated_on = models.IntegerField()
    created_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_modules_notification'


class InfogeonNotifications(models.Model):
    ntid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=512, blank=True, null=True)
    entity_id = models.PositiveIntegerField()
    id = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    timestmp = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_notifications'


class InfogeonPulseCheckAnswers(models.Model):
    pcaid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    guid = models.CharField(max_length=255)
    uid = models.PositiveIntegerField()
    pcqid = models.PositiveIntegerField()
    answer_text = models.CharField(max_length=60, blank=True, null=True)
    answer_number = models.FloatField(blank=True, null=True)
    uploaded_date = models.IntegerField(blank=True, null=True)
    answer_date = models.IntegerField(blank=True, null=True)
    answered = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_pulse_check_answers'


class InfogeonPulseCheckQuestionRelation(models.Model):
    pcqrid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    pcqid = models.PositiveIntegerField()
    gid = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_pulse_check_question_relation'


class InfogeonPulseCheckQuestions(models.Model):
    pcqid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    guid = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    question_type = models.PositiveIntegerField(blank=True, null=True)
    assigned_group = models.CharField(max_length=50)
    created_by = models.PositiveIntegerField()
    uploaded_date = models.IntegerField(blank=True, null=True)
    created_date = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_pulse_check_questions'


class InfogeonQuizResult(models.Model):
    qid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    uid = models.IntegerField()
    mid = models.IntegerField()
    docid = models.IntegerField()
    info = models.TextField()
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_quiz_result'


class InfogeonQzGroup(models.Model):
    grp_id = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    grp_name = models.CharField(max_length=200, blank=True, null=True)
    grp_desc = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.IntegerField()
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_qz_group'


class InfogeonQzGroupModule(models.Model):
    module_grp_id = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    module_grp_name = models.CharField(max_length=200, blank=True, null=True)
    module_grp_desc = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.IntegerField()
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_qz_group_module'


class InfogeonQzMapping(models.Model):
    cmid = models.PositiveIntegerField()
    grp_id = models.PositiveIntegerField()
    qz_id = models.PositiveIntegerField()
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_qz_mapping'


class InfogeonQzModuleMapping(models.Model):
    cmid = models.PositiveIntegerField()
    grp_id = models.PositiveIntegerField()
    qz_id = models.PositiveIntegerField()
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_qz_module_mapping'


class InfogeonQzOptions(models.Model):
    opt_id = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    qz_options = models.CharField(max_length=255, blank=True, null=True)
    qz_question_id = models.PositiveIntegerField()
    qz_answer = models.CharField(max_length=255, blank=True, null=True)
    qz_answer_score = models.IntegerField(blank=True, null=True)
    qz_answer_score_dec = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_qz_options'


class InfogeonQzQuestions(models.Model):
    qz_id = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    qz_type = models.CharField(max_length=200, blank=True, null=True)
    qz_question = models.CharField(max_length=255, blank=True, null=True)
    qa_image_path = models.CharField(max_length=255, blank=True, null=True)
    qz_weight = models.IntegerField(blank=True, null=True)
    qz_tags = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_qz_questions'


class InfogeonQzSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    entity_id = models.IntegerField()
    end_date = models.IntegerField(blank=True, null=True)
    time_limit_min = models.IntegerField(blank=True, null=True)
    time_limit_sec = models.IntegerField(blank=True, null=True)
    total_time_allocation = models.CharField(max_length=225, blank=True, null=True)
    passing_score = models.FloatField(blank=True, null=True)
    number_of_attempt = models.IntegerField(blank=True, null=True)
    feedback_option = models.IntegerField(blank=True, null=True)
    shuffle_question = models.IntegerField(blank=True, null=True)
    shuffle_answer = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updated_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_qz_settings'


class InfogeonQzTotalScore(models.Model):
    score_id = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    entity_id = models.IntegerField()
    uid = models.IntegerField()
    score = models.FloatField()
    taken_time = models.IntegerField()
    guid = models.CharField(max_length=255)
    updated_time = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_qz_total_score'


class InfogeonReportsSubmitNotification(models.Model):
    rnid = models.AutoField(primary_key=True)
    rid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    cmid = models.PositiveIntegerField()
    suid = models.PositiveIntegerField()
    submitter_uid = models.IntegerField()
    puid = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_reports_submit_notification'


class InfogeonSections(models.Model):
    secid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    section_name = models.CharField(max_length=255)
    section_image = models.IntegerField()
    section_desc = models.CharField(max_length=255)
    section_tags = models.CharField(max_length=255)
    is_completed = models.IntegerField()
    created_on = models.IntegerField()
    updated_on = models.IntegerField()
    created_by = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_sections'


class InfogeonShareReports(models.Model):
    cmid = models.PositiveIntegerField()
    entity_id = models.IntegerField()
    entity_type = models.CharField(max_length=255)
    assigned_to = models.IntegerField()
    assigned_by = models.IntegerField()
    assigned_on = models.IntegerField()
    updated_on = models.IntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_share_reports'


class InfogeonTrainingScoreInfo(models.Model):
    isid = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    mid = models.IntegerField()
    uid = models.IntegerField()
    docid = models.IntegerField()
    score = models.IntegerField()
    taken_date = models.IntegerField()
    device_info = models.IntegerField()
    guid = models.CharField(max_length=255)
    updated_on = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_training_score_info'


class InfogeonUsers(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    cmid = models.PositiveIntegerField()
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    role = models.PositiveIntegerField(blank=True, null=True)
    invited_by = models.IntegerField()
    approved_by = models.IntegerField()
    approved_on = models.IntegerField()
    blocked_by = models.IntegerField()
    blocked_date = models.IntegerField()
    denied_by = models.IntegerField()
    old_email = models.CharField(max_length=255)
    old_mobile = models.CharField(max_length=60)
    country_code = models.CharField(max_length=10)
    email_valid_req = models.IntegerField()
    mobile_otp = models.IntegerField()
    email_otp = models.IntegerField()
    invited_date = models.IntegerField(blank=True, null=True)
    bsharp_insights = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_users'


class InfogeonUsersApprovalStatus(models.Model):
    approval_id = models.AutoField(primary_key=True)
    cmid = models.IntegerField()
    invite_approval_status = models.IntegerField()
    validate_email_status = models.IntegerField()
    updated_by = models.IntegerField()
    action_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infogeon_users_approval_status'


class InfogeonUsersAttributes(models.Model):
    uaid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    aid = models.PositiveIntegerField()
    aoid = models.PositiveIntegerField()
    attribute_value = models.CharField(max_length=100, blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_users_attributes'


class InfogeonUsersGroup(models.Model):
    ugid = models.AutoField(primary_key=True)
    cmid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    gid = models.PositiveIntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_users_group'


class InfogeonUsersLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=100, blank=True, null=True)
    action_date = models.CharField(max_length=50, blank=True, null=True)
    cmid = models.IntegerField(blank=True, null=True)
    action_from = models.IntegerField(blank=True, null=True)
    action_to = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infogeon_users_logs'


class InfognInfocaptureTemplate(models.Model):
    itid = models.AutoField(primary_key=True)
    nid = models.PositiveIntegerField()
    thumb_fid = models.PositiveIntegerField()
    preview_fid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'infogn_infocapture_template'


class Languages(models.Model):
    language = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=64)
    native = models.CharField(max_length=64)
    direction = models.IntegerField()
    enabled = models.IntegerField()
    plurals = models.IntegerField()
    formula = models.CharField(max_length=255)
    domain = models.CharField(max_length=128)
    prefix = models.CharField(max_length=128)
    weight = models.IntegerField()
    javascript = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'languages'


class LocalesSource(models.Model):
    lid = models.AutoField(primary_key=True)
    location = models.TextField(blank=True, null=True)
    textgroup = models.CharField(max_length=255)
    source = models.TextField()
    context = models.CharField(max_length=255)
    version = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'locales_source'


class LocalesTarget(models.Model):
    lid = models.IntegerField()
    translation = models.TextField()
    language = models.CharField(max_length=12)
    plid = models.IntegerField()
    plural = models.IntegerField()
    i18n_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locales_target'
        unique_together = (('language', 'lid', 'plural'),)


class LogInfo(models.Model):
    lid = models.AutoField(primary_key=True)
    function_name = models.CharField(max_length=512, blank=True, null=True)
    function_start_time = models.BigIntegerField(blank=True, null=True)
    function_end_time = models.BigIntegerField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_info'


class MenuCustom(models.Model):
    menu_name = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_custom'


class MenuLinks(models.Model):
    menu_name = models.CharField(max_length=32)
    mlid = models.AutoField(primary_key=True)
    plid = models.PositiveIntegerField()
    link_path = models.CharField(max_length=255)
    router_path = models.CharField(max_length=255)
    link_title = models.CharField(max_length=255)
    options = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=255)
    hidden = models.SmallIntegerField()
    external = models.SmallIntegerField()
    has_children = models.SmallIntegerField()
    expanded = models.SmallIntegerField()
    weight = models.IntegerField()
    depth = models.SmallIntegerField()
    customized = models.SmallIntegerField()
    p1 = models.PositiveIntegerField()
    p2 = models.PositiveIntegerField()
    p3 = models.PositiveIntegerField()
    p4 = models.PositiveIntegerField()
    p5 = models.PositiveIntegerField()
    p6 = models.PositiveIntegerField()
    p7 = models.PositiveIntegerField()
    p8 = models.PositiveIntegerField()
    p9 = models.PositiveIntegerField()
    updated = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'menu_links'


class MenuRouter(models.Model):
    path = models.CharField(primary_key=True, max_length=255)
    load_functions = models.TextField()
    to_arg_functions = models.TextField()
    access_callback = models.CharField(max_length=255)
    access_arguments = models.TextField(blank=True, null=True)
    page_callback = models.CharField(max_length=255)
    page_arguments = models.TextField(blank=True, null=True)
    delivery_callback = models.CharField(max_length=255)
    fit = models.IntegerField()
    number_parts = models.SmallIntegerField()
    context = models.IntegerField()
    tab_parent = models.CharField(max_length=255)
    tab_root = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_callback = models.CharField(max_length=255)
    title_arguments = models.CharField(max_length=255)
    theme_callback = models.CharField(max_length=255)
    theme_arguments = models.CharField(max_length=255)
    type = models.IntegerField()
    description = models.TextField()
    position = models.CharField(max_length=255)
    weight = models.IntegerField()
    include_file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_router'


class Node(models.Model):
    nid = models.AutoField(primary_key=True)
    vid = models.PositiveIntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=32)
    language = models.CharField(max_length=12)
    title = models.CharField(max_length=255)
    uid = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField()
    changed = models.IntegerField()
    comment = models.IntegerField()
    promote = models.IntegerField()
    sticky = models.IntegerField()
    tnid = models.PositiveIntegerField()
    translate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node'


class NodeAccess(models.Model):
    nid = models.PositiveIntegerField()
    gid = models.PositiveIntegerField()
    realm = models.CharField(max_length=255)
    grant_view = models.PositiveIntegerField()
    grant_update = models.PositiveIntegerField()
    grant_delete = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_access'
        unique_together = (('nid', 'gid', 'realm'),)


class NodeCommentStatistics(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    cid = models.IntegerField()
    last_comment_timestamp = models.IntegerField()
    last_comment_name = models.CharField(max_length=60, blank=True, null=True)
    last_comment_uid = models.IntegerField()
    comment_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_comment_statistics'


class NodeRevision(models.Model):
    nid = models.PositiveIntegerField()
    vid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    title = models.CharField(max_length=255)
    log = models.TextField()
    timestamp = models.IntegerField()
    status = models.IntegerField()
    comment = models.IntegerField()
    promote = models.IntegerField()
    sticky = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_revision'


class NodeType(models.Model):
    type = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    base = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    description = models.TextField()
    help = models.TextField()
    has_title = models.PositiveIntegerField()
    title_label = models.CharField(max_length=255)
    custom = models.IntegerField()
    modified = models.IntegerField()
    locked = models.IntegerField()
    disabled = models.IntegerField()
    orig_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_type'


class NotificationsInfo(models.Model):
    nitid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    entity_type = models.CharField(max_length=512, blank=True, null=True)
    entity_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications_info'


class PageManagerHandlers(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    task = models.CharField(max_length=64, blank=True, null=True)
    subtask = models.CharField(max_length=64)
    handler = models.CharField(max_length=64, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    conf = models.TextField()

    class Meta:
        managed = False
        db_table = 'page_manager_handlers'


class PageManagerPages(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    task = models.CharField(max_length=64, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    access = models.TextField()
    menu = models.TextField()
    arguments = models.TextField()
    conf = models.TextField()

    class Meta:
        managed = False
        db_table = 'page_manager_pages'


class PageManagerWeights(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page_manager_weights'


class PushNotificationsQueue(models.Model):
    uid = models.IntegerField(primary_key=True)
    payload = models.CharField(max_length=256)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'push_notifications_queue'


class PushNotificationsTokens(models.Model):
    token = models.CharField(max_length=255)
    uid = models.IntegerField()
    type = models.IntegerField()
    timestamp = models.IntegerField()
    language = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'push_notifications_tokens'
        unique_together = (('token', 'uid'),)


class Queue(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'queue'


class RdfMapping(models.Model):
    type = models.CharField(max_length=128)
    bundle = models.CharField(max_length=128)
    mapping = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rdf_mapping'
        unique_together = (('type', 'bundle'),)


class Registry(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=9)
    filename = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registry'
        unique_together = (('name', 'type'),)


class RegistryFile(models.Model):
    filename = models.CharField(primary_key=True, max_length=255)
    hash = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'registry_file'


class Role(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role'


class RolePermission(models.Model):
    rid = models.PositiveIntegerField()
    permission = models.CharField(max_length=128)
    module = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role_permission'
        unique_together = (('rid', 'permission'),)


class SearchDataset(models.Model):
    sid = models.PositiveIntegerField()
    type = models.CharField(max_length=16)
    data = models.TextField()
    reindex = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'search_dataset'
        unique_together = (('sid', 'type'),)


class SearchIndex(models.Model):
    word = models.CharField(max_length=50)
    sid = models.PositiveIntegerField()
    type = models.CharField(max_length=16)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_index'
        unique_together = (('word', 'sid', 'type'),)


class SearchNodeLinks(models.Model):
    sid = models.PositiveIntegerField()
    type = models.CharField(max_length=16)
    nid = models.PositiveIntegerField()
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_node_links'
        unique_together = (('sid', 'type', 'nid'),)


class SearchTotal(models.Model):
    word = models.CharField(primary_key=True, max_length=50)
    count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_total'


class Semaphore(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)
    expire = models.FloatField()

    class Meta:
        managed = False
        db_table = 'semaphore'


class Sequences(models.Model):
    value = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sequences'


class ServicesEndpoint(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    server = models.CharField(max_length=32)
    path = models.CharField(max_length=255)
    authentication = models.TextField()
    server_settings = models.TextField()
    resources = models.TextField()
    debug = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services_endpoint'


class ServicesUser(models.Model):
    uid = models.PositiveIntegerField()
    created = models.IntegerField()
    changed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services_user'


class Sessions(models.Model):
    uid = models.PositiveIntegerField()
    sid = models.CharField(max_length=128)
    ssid = models.CharField(max_length=128)
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()
    cache = models.IntegerField()
    session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'
        unique_together = (('sid', 'ssid'),)


class ShortcutSet(models.Model):
    set_name = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shortcut_set'


class ShortcutSetUsers(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    set_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'shortcut_set_users'


class System(models.Model):
    filename = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=12)
    owner = models.CharField(max_length=255)
    status = models.IntegerField()
    bootstrap = models.IntegerField()
    schema_version = models.SmallIntegerField()
    weight = models.IntegerField()
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system'


class TableAccess(models.Model):
    taid = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    grant_select = models.PositiveIntegerField(blank=True, null=True)
    grant_delete = models.PositiveIntegerField(blank=True, null=True)
    grant_update = models.PositiveIntegerField(blank=True, null=True)
    grant_alter = models.PositiveIntegerField(blank=True, null=True)
    grant_drop = models.PositiveIntegerField(blank=True, null=True)
    grant_insert = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_access'


class TaxonomyIndex(models.Model):
    nid = models.PositiveIntegerField()
    tid = models.PositiveIntegerField()
    sticky = models.IntegerField(blank=True, null=True)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_index'


class TaxonomyTermData(models.Model):
    tid = models.AutoField(primary_key=True)
    vid = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_term_data'


class TaxonomyTermHierarchy(models.Model):
    tid = models.PositiveIntegerField()
    parent = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_term_hierarchy'
        unique_together = (('tid', 'parent'),)


class TaxonomyVocabulary(models.Model):
    vid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    machine_name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    hierarchy = models.PositiveIntegerField()
    module = models.CharField(max_length=255)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_vocabulary'


class UrlAlias(models.Model):
    pid = models.AutoField(primary_key=True)
    source = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'url_alias'


class UserCompanyRelation(models.Model):
    ucrid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    cmid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'user_company_relation'


class Userpoints(models.Model):
    pid = models.IntegerField()
    uid = models.IntegerField()
    points = models.IntegerField()
    max_points = models.IntegerField()
    last_update = models.IntegerField()
    tid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userpoints'


class UserpointsTotal(models.Model):
    uid = models.IntegerField()
    points = models.IntegerField()
    max_points = models.IntegerField()
    last_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userpoints_total'


class UserpointsTxn(models.Model):
    txn_id = models.IntegerField()
    uid = models.IntegerField()
    approver_uid = models.IntegerField()
    points = models.IntegerField()
    time_stamp = models.IntegerField()
    changed = models.IntegerField()
    status = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=128, blank=True, null=True)
    expirydate = models.IntegerField()
    expired = models.IntegerField()
    parent_txn_id = models.IntegerField()
    tid = models.IntegerField()
    entity_id = models.IntegerField()
    entity_type = models.CharField(max_length=128, blank=True, null=True)
    operation = models.CharField(max_length=48, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userpoints_txn'


class Users(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    pass_field = models.CharField(db_column='pass', max_length=128)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=254, blank=True, null=True)
    theme = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)
    signature_format = models.CharField(max_length=255, blank=True, null=True)
    created = models.IntegerField()
    access = models.IntegerField()
    login = models.IntegerField()
    status = models.IntegerField()
    timezone = models.CharField(max_length=32, blank=True, null=True)
    language = models.CharField(max_length=12)
    picture = models.IntegerField()
    init = models.CharField(max_length=254, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersRoles(models.Model):
    uid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'users_roles'
        unique_together = (('uid', 'rid'),)


class Variable(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'variable'


class ViewsDisplay(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    id = models.CharField(max_length=64)
    display_title = models.CharField(max_length=64)
    display_plugin = models.CharField(max_length=64)
    position = models.IntegerField(blank=True, null=True)
    display_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_display'
        unique_together = (('vid', 'id'),)


class ViewsView(models.Model):
    vid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    description = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    base_table = models.CharField(max_length=64)
    human_name = models.CharField(max_length=255, blank=True, null=True)
    core = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_view'


class Watchdog(models.Model):
    wid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    type = models.CharField(max_length=64)
    message = models.TextField()
    variables = models.TextField()
    severity = models.PositiveIntegerField()
    link = models.CharField(max_length=255, blank=True, null=True)
    location = models.TextField()
    referer = models.TextField(blank=True, null=True)
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'watchdog'


class Webform(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    next_serial = models.PositiveIntegerField()
    confirmation = models.TextField()
    confirmation_format = models.CharField(max_length=255, blank=True, null=True)
    redirect_url = models.CharField(max_length=2048, blank=True, null=True)
    status = models.IntegerField()
    block = models.IntegerField()
    allow_draft = models.IntegerField()
    auto_save = models.IntegerField()
    submit_notice = models.IntegerField()
    confidential = models.IntegerField()
    submit_text = models.CharField(max_length=255, blank=True, null=True)
    submit_limit = models.IntegerField()
    submit_interval = models.IntegerField()
    total_submit_limit = models.IntegerField()
    total_submit_interval = models.IntegerField()
    progressbar_bar = models.IntegerField()
    progressbar_page_number = models.IntegerField()
    progressbar_percent = models.IntegerField()
    progressbar_pagebreak_labels = models.IntegerField()
    progressbar_include_confirmation = models.IntegerField()
    progressbar_label_first = models.CharField(max_length=255, blank=True, null=True)
    progressbar_label_confirmation = models.CharField(max_length=255, blank=True, null=True)
    preview = models.IntegerField()
    preview_next_button_label = models.CharField(max_length=255, blank=True, null=True)
    preview_prev_button_label = models.CharField(max_length=255, blank=True, null=True)
    preview_title = models.CharField(max_length=255, blank=True, null=True)
    preview_message = models.TextField()
    preview_message_format = models.CharField(max_length=255, blank=True, null=True)
    preview_excluded_components = models.TextField()
    machine_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webform'


class WebformComponent(models.Model):
    nid = models.PositiveIntegerField()
    cid = models.PositiveSmallIntegerField()
    pid = models.PositiveSmallIntegerField()
    form_key = models.CharField(max_length=128, blank=True, null=True)
    name = models.TextField()
    type = models.CharField(max_length=16, blank=True, null=True)
    value = models.TextField()
    extra = models.TextField()
    required = models.IntegerField()
    weight = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'webform_component'
        unique_together = (('nid', 'cid'),)


class WebformComponentLocalization(models.Model):
    nid = models.PositiveIntegerField()
    cid = models.PositiveSmallIntegerField()
    standar_properties = models.TextField()
    extra_properties = models.TextField()

    class Meta:
        managed = False
        db_table = 'webform_component_localization'


class WebformConditional(models.Model):
    nid = models.PositiveIntegerField()
    rgid = models.PositiveSmallIntegerField()
    andor = models.CharField(max_length=128, blank=True, null=True)
    weight = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'webform_conditional'
        unique_together = (('nid', 'rgid'),)


class WebformConditionalActions(models.Model):
    nid = models.PositiveIntegerField()
    rgid = models.PositiveSmallIntegerField()
    aid = models.PositiveSmallIntegerField()
    target_type = models.CharField(max_length=128, blank=True, null=True)
    target = models.CharField(max_length=128, blank=True, null=True)
    invert = models.PositiveSmallIntegerField()
    action = models.CharField(max_length=128, blank=True, null=True)
    argument = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webform_conditional_actions'
        unique_together = (('nid', 'rgid', 'aid'),)


class WebformConditionalRules(models.Model):
    nid = models.PositiveIntegerField()
    rgid = models.PositiveSmallIntegerField()
    rid = models.PositiveSmallIntegerField()
    source_type = models.CharField(max_length=128, blank=True, null=True)
    source = models.PositiveSmallIntegerField()
    operator = models.CharField(max_length=128, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webform_conditional_rules'
        unique_together = (('nid', 'rgid', 'rid'),)


class WebformEmails(models.Model):
    nid = models.PositiveIntegerField()
    eid = models.PositiveSmallIntegerField()
    email = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    from_name = models.TextField(blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    excluded_components = models.TextField()
    html = models.PositiveIntegerField()
    attachments = models.PositiveIntegerField()
    exclude_empty = models.PositiveIntegerField()
    extra = models.TextField()

    class Meta:
        managed = False
        db_table = 'webform_emails'
        unique_together = (('nid', 'eid'),)


class WebformLastDownload(models.Model):
    nid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    requested = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'webform_last_download'
        unique_together = (('nid', 'uid'),)


class WebformLocalization(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    expose_strings = models.IntegerField()
    single_webform = models.IntegerField()
    webform_properties = models.TextField()
    sync_components = models.IntegerField()
    sync_roles = models.IntegerField()
    sync_emails = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'webform_localization'


class WebformRoles(models.Model):
    nid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'webform_roles'
        unique_together = (('nid', 'rid'),)


class WebformSubmissions(models.Model):
    sid = models.AutoField(primary_key=True)
    nid = models.PositiveIntegerField()
    serial = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    is_draft = models.IntegerField()
    highest_valid_page = models.SmallIntegerField()
    submitted = models.IntegerField()
    completed = models.IntegerField()
    modified = models.IntegerField()
    remote_addr = models.CharField(max_length=128, blank=True, null=True)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'webform_submissions'
        unique_together = (('sid', 'nid'), ('nid', 'serial'),)


class WebformSubmittedData(models.Model):
    nid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    cid = models.PositiveSmallIntegerField()
    no = models.CharField(max_length=128)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'webform_submitted_data'
        unique_together = (('nid', 'sid', 'cid', 'no'),)
