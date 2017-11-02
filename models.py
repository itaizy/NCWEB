# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ComplainBackup(models.Model):
    doid = models.IntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    atuid = models.IntegerField()
    atuname = models.CharField(max_length=100)
    isreply = models.IntegerField()
    addtime = models.IntegerField()
    dateline = models.IntegerField()
    replytime = models.IntegerField()
    expire = models.IntegerField()
    times = models.IntegerField()
    atdepartment = models.CharField(max_length=255)
    atdeptuid = models.IntegerField()
    issendmsg = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    datatime = models.CharField(max_length=45, blank=True, null=True)
    ontrack = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    curuid = models.IntegerField(blank=True, null=True)
    curusername = models.CharField(max_length=20, blank=True, null=True)
    lastopoid = models.PositiveIntegerField(blank=True, null=True)
    relay_times = models.IntegerField(blank=True, null=True)
    relayed_by = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain_backup'


class ComplainBak(models.Model):
    doid = models.IntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    atuid = models.IntegerField()
    atuname = models.CharField(max_length=100)
    isreply = models.IntegerField()
    addtime = models.IntegerField()
    dateline = models.IntegerField()
    replytime = models.IntegerField()
    expire = models.IntegerField()
    times = models.IntegerField()
    atdepartment = models.CharField(max_length=255)
    atdeptuid = models.IntegerField()
    issendmsg = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    datatime = models.CharField(max_length=45, blank=True, null=True)
    ontrack = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    curuid = models.IntegerField(blank=True, null=True)
    curusername = models.CharField(max_length=20, blank=True, null=True)
    lastopoid = models.PositiveIntegerField(blank=True, null=True)
    relay_times = models.IntegerField(blank=True, null=True)
    relayed_by = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain_bak'


class ComplainSave(models.Model):
    doid = models.IntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    atuid = models.IntegerField()
    atuname = models.CharField(max_length=100)
    isreply = models.IntegerField()
    addtime = models.IntegerField()
    dateline = models.IntegerField()
    replytime = models.IntegerField()
    expire = models.IntegerField()
    times = models.IntegerField()
    atdepartment = models.CharField(max_length=255)
    atdeptuid = models.IntegerField()
    issendmsg = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    datatime = models.CharField(max_length=45, blank=True, null=True)
    ontrack = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    curuid = models.IntegerField(blank=True, null=True)
    curusername = models.CharField(max_length=20, blank=True, null=True)
    lastopoid = models.PositiveIntegerField(blank=True, null=True)
    relay_times = models.IntegerField(blank=True, null=True)
    relayed_by = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain_save'


class Complaint(models.Model):
    uid = models.IntegerField()
    doid = models.IntegerField()
    id = models.IntegerField()
    addtime = models.IntegerField()
    replytime = models.IntegerField()
    atdepartment = models.CharField(max_length=255)
    atdeptuid = models.IntegerField()
    message = models.CharField(max_length=280, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint'


class IauthApiInfo(models.Model):
    api_id = models.PositiveIntegerField()
    hash = models.CharField(primary_key=True, max_length=40)
    api_type = models.CharField(max_length=14)
    api_url = models.CharField(max_length=255)
    forward_url = models.CharField(max_length=255)
    owner_id = models.CharField(max_length=16)
    status = models.CharField(max_length=7, blank=True, null=True)
    api_name = models.CharField(max_length=48, blank=True, null=True)
    limit_seconds = models.PositiveIntegerField()
    limit_counts = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'iauth_api_info'


class IauthAppInfo(models.Model):
    app_id = models.CharField(primary_key=True, max_length=16)
    app_secret = models.CharField(max_length=48)
    app_type = models.CharField(max_length=3, blank=True, null=True)
    auto_auth = models.IntegerField()
    status = models.CharField(max_length=7, blank=True, null=True)
    app_name = models.CharField(max_length=48, blank=True, null=True)
    call_back = models.CharField(max_length=255, blank=True, null=True)
    login_url = models.CharField(max_length=255, blank=True, null=True)
    ip_check = models.CharField(max_length=7, blank=True, null=True)
    session_init = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iauth_app_info'


class IauthAuthToken(models.Model):
    app_id = models.CharField(max_length=16)
    user_id = models.PositiveIntegerField()
    rights = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=48, blank=True, null=True)
    access_secret = models.CharField(max_length=48, blank=True, null=True)
    create_t = models.DateTimeField()
    faile_t = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'iauth_auth_token'
        unique_together = (('app_id', 'user_id', 'access_token', 'access_secret'),)


class IauthErrorLog(models.Model):
    error_id = models.AutoField(primary_key=True)
    error_time = models.DateTimeField()
    error_ip = models.CharField(max_length=60)
    error_appid = models.CharField(max_length=16)
    error_message = models.CharField(max_length=255)
    error_detail = models.CharField(max_length=2048)
    error_stack = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'iauth_error_log'


class IauthRequestNonce(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField(max_length=16)
    target_id = models.PositiveIntegerField()
    rtype = models.CharField(max_length=6)
    ip = models.CharField(max_length=48)
    content = models.CharField(max_length=255)
    nonce = models.CharField(max_length=16)
    create_t = models.DateTimeField()
    faile_t = models.DateTimeField()
    state = models.CharField(max_length=16)
    status = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'iauth_request_nonce'


class IhomeAppfpnews(models.Model):
    picurl = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_AppFPnews'


class IhomeActionlog(models.Model):
    uid = models.PositiveIntegerField()
    action = models.CharField(max_length=20)
    value = models.CharField(max_length=200)
    dateline = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_actionlog'


class IhomeAd(models.Model):
    adid = models.PositiveSmallIntegerField(primary_key=True)
    available = models.IntegerField()
    title = models.CharField(max_length=50)
    pagetype = models.CharField(max_length=20)
    adcode = models.TextField()
    system = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_ad'


class IhomeAd4App(models.Model):
    img = models.CharField(max_length=60)
    url = models.CharField(max_length=255)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_ad4app'


class IhomeAd4Dev(models.Model):
    display = models.IntegerField()
    seq = models.IntegerField()
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=64, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_ad4dev'


class IhomeAdminsession(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    ip = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    errorcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_adminsession'


class IhomeAlbum(models.Model):
    albumid = models.AutoField(primary_key=True)
    albumname = models.CharField(max_length=50)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    updatetime = models.PositiveIntegerField()
    picnum = models.PositiveSmallIntegerField()
    pic = models.CharField(max_length=60)
    picflag = models.IntegerField()
    friend = models.IntegerField()
    password = models.CharField(max_length=10)
    target_ids = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_album'


class IhomeApi(models.Model):
    iauthenname = models.CharField(db_column='iauthENname', max_length=48)  # Field name made lowercase.
    iauthapiid = models.IntegerField(db_column='iauthAPIid')  # Field name made lowercase.
    appid = models.CharField(max_length=18)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=15)
    fullname = models.CharField(max_length=120, blank=True, null=True)
    intro = models.CharField(max_length=255, blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ihome_api'


class IhomeApisms(models.Model):
    smsid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    username = models.CharField(max_length=30)
    tomobile = models.CharField(max_length=40)
    mssage = models.TextField()
    sendtime = models.IntegerField()
    addtime = models.IntegerField()
    status = models.IntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_apisms'


class IhomeAppcreditlog(models.Model):
    logid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    appid = models.PositiveIntegerField()
    appname = models.CharField(max_length=60)
    type = models.IntegerField()
    credit = models.PositiveIntegerField()
    note = models.TextField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_appcreditlog'


class IhomeApps(models.Model):
    iauth_id = models.CharField(max_length=18, blank=True, null=True)
    iauth_secret = models.CharField(max_length=255, blank=True, null=True)
    iauth_type = models.CharField(max_length=10, blank=True, null=True)
    iauth_name = models.CharField(max_length=48, blank=True, null=True)
    name = models.CharField(max_length=20)
    logo = models.CharField(max_length=60)
    desc = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    app_url = models.CharField(max_length=255, blank=True, null=True)
    back_url = models.CharField(max_length=255, blank=True, null=True)
    app_pkg = models.CharField(max_length=60, blank=True, null=True)
    category = models.IntegerField()
    usertype = models.CharField(max_length=100)
    starttime = models.IntegerField()
    endtime = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    useapi = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    ishidden = models.IntegerField()
    promote = models.IntegerField()
    applypass = models.IntegerField()
    applyuid = models.IntegerField()
    applytime = models.IntegerField()
    applyip = models.CharField(max_length=15)
    views = models.IntegerField(blank=True, null=True)
    usernumber = models.IntegerField(blank=True, null=True)
    clicktime = models.IntegerField(blank=True, null=True)
    modders = models.IntegerField(blank=True, null=True)
    comment = models.IntegerField()
    score = models.FloatField(blank=True, null=True)
    score_easy = models.FloatField(blank=True, null=True)
    score_service = models.FloatField(blank=True, null=True)
    offline = models.IntegerField()
    log = models.TextField(blank=True, null=True)
    score_speed = models.FloatField(blank=True, null=True)
    s = models.BigIntegerField(db_column='S', blank=True, null=True)  # Field name made lowercase.
    se = models.BigIntegerField(db_column='SE', blank=True, null=True)  # Field name made lowercase.
    sv = models.BigIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    sp = models.BigIntegerField(db_column='SP', blank=True, null=True)  # Field name made lowercase.
    scorer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_apps'


class IhomeAppsDetail(models.Model):
    appsid = models.IntegerField()
    uid = models.IntegerField()
    anonymous = models.IntegerField()
    score = models.FloatField()
    score_easy = models.FloatField()
    score_service = models.FloatField()
    score_speed = models.FloatField()
    content = models.TextField()
    ip = models.CharField(max_length=64)
    time = models.IntegerField()
    vision = models.CharField(max_length=20)
    issystem = models.IntegerField()
    upvotes = models.IntegerField(blank=True, null=True)
    voter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_apps_detail'
        unique_together = (('id', 'appsid', 'uid'),)


class IhomeAppsUsers(models.Model):
    uid = models.IntegerField()
    appsid = models.SmallIntegerField()
    clicktime = models.SmallIntegerField()
    shortcut = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_apps_users'


class IhomeAppversion(models.Model):
    app_url = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)
    version = models.CharField(max_length=50)
    time = models.DateTimeField()
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ihome_appversion'


class IhomeArrangement(models.Model):
    arrangementid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    classid = models.PositiveSmallIntegerField()
    starttime = models.PositiveIntegerField()
    message = models.TextField()
    tag = models.CharField(max_length=255)
    postip = models.CharField(max_length=20)
    viewnum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    dateline = models.IntegerField()
    pic = models.CharField(max_length=120)
    picflag = models.IntegerField()
    noreply = models.IntegerField()
    click_1 = models.SmallIntegerField()
    click_2 = models.SmallIntegerField()
    click_3 = models.SmallIntegerField()
    click_4 = models.SmallIntegerField()
    click_5 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_arrangement'


class IhomeAsst(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    name = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.CharField(max_length=10, blank=True, null=True)
    applydate = models.CharField(max_length=10)
    passdate = models.CharField(max_length=10, blank=True, null=True)
    degree = models.CharField(max_length=45, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    academy = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    pass_uid = models.PositiveIntegerField()
    passed = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_asst'
        unique_together = (('uid', 'applydate'),)


class IhomeAttach(models.Model):
    aid = models.AutoField(primary_key=True)
    albumid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    postip = models.CharField(max_length=20)
    filename = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    size = models.PositiveIntegerField()
    filepath = models.CharField(max_length=60)
    desc = models.CharField(max_length=400)
    dltime = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_attach'


class IhomeAutorecpub(models.Model):
    uid = models.PositiveIntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    recto = models.TextField(db_column='recTo', blank=True, null=True)  # Field name made lowercase.
    exclude = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_autorecpub'


class IhomeBaseemail(models.Model):
    userid = models.AutoField(primary_key=True)
    collegeid = models.CharField(max_length=30)
    email = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseemail'


class IhomeBaseprofile(models.Model):
    userid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    isactive = models.IntegerField()
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier_not_use = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    shortemail = models.CharField(max_length=40, blank=True, null=True)
    aliasemail = models.CharField(max_length=100, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    emaildateline = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    workprovince = models.CharField(max_length=30, blank=True, null=True)
    workcity = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.PositiveIntegerField(blank=True, null=True)
    comingtime = models.CharField(max_length=16, blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    invite_or_not = models.IntegerField(blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseprofile'


class IhomeBaseprofile201703212(models.Model):
    userid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    isactive = models.IntegerField()
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier_not_use = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    shortemail = models.CharField(max_length=40, blank=True, null=True)
    aliasemail = models.CharField(max_length=100, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    emaildateline = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    workprovince = models.CharField(max_length=30, blank=True, null=True)
    workcity = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.PositiveIntegerField(blank=True, null=True)
    comingtime = models.CharField(max_length=16, blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    invite_or_not = models.IntegerField(blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseprofile_201703212'


class IhomeBaseprofile20170714(models.Model):
    userid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    isactive = models.IntegerField()
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier_not_use = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    shortemail = models.CharField(max_length=40, blank=True, null=True)
    aliasemail = models.CharField(max_length=100, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    emaildateline = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    workprovince = models.CharField(max_length=30, blank=True, null=True)
    workcity = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.PositiveIntegerField(blank=True, null=True)
    comingtime = models.CharField(max_length=16, blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    invite_or_not = models.IntegerField(blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseprofile_20170714'


class IhomeBaseprofile20170717(models.Model):
    userid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    isactive = models.IntegerField()
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier_not_use = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    shortemail = models.CharField(max_length=40, blank=True, null=True)
    aliasemail = models.CharField(max_length=100, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    emaildateline = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    workprovince = models.CharField(max_length=30, blank=True, null=True)
    workcity = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.PositiveIntegerField(blank=True, null=True)
    comingtime = models.CharField(max_length=16, blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    invite_or_not = models.IntegerField(blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseprofile_20170717'


class IhomeBaseprofile20170913(models.Model):
    userid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    isactive = models.IntegerField()
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier_not_use = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    shortemail = models.CharField(max_length=40, blank=True, null=True)
    aliasemail = models.CharField(max_length=100, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    emaildateline = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    workprovince = models.CharField(max_length=30, blank=True, null=True)
    workcity = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.PositiveIntegerField(blank=True, null=True)
    comingtime = models.CharField(max_length=16, blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    invite_or_not = models.IntegerField(blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseprofile_20170913'


class IhomeBaseprofile20171010(models.Model):
    userid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    isactive = models.IntegerField()
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier_not_use = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    shortemail = models.CharField(max_length=40, blank=True, null=True)
    aliasemail = models.CharField(max_length=100, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    emaildateline = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    workprovince = models.CharField(max_length=30, blank=True, null=True)
    workcity = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.PositiveIntegerField(blank=True, null=True)
    comingtime = models.CharField(max_length=16, blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    invite_or_not = models.IntegerField(blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_baseprofile_20171010'


class IhomeBind(models.Model):
    uid = models.IntegerField()
    sso_name = models.CharField(max_length=20)
    sso_status = models.IntegerField()
    token = models.CharField(max_length=64)
    tokentime = models.DateTimeField()
    tokenstatus = models.IntegerField()
    token1 = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'ihome_bind'


class IhomeBlacklist(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    buid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_blacklist'
        unique_together = (('uid', 'buid'),)


class IhomeBlock(models.Model):
    bid = models.PositiveSmallIntegerField(primary_key=True)
    blockname = models.CharField(max_length=40)
    blocksql = models.TextField()
    cachename = models.CharField(max_length=30)
    cachetime = models.PositiveSmallIntegerField()
    startnum = models.PositiveIntegerField()
    num = models.PositiveIntegerField()
    perpage = models.PositiveIntegerField()
    htmlcode = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_block'


class IhomeBlog(models.Model):
    blogid = models.AutoField(primary_key=True)
    topicid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    subject = models.CharField(max_length=80)
    classid = models.PositiveSmallIntegerField()
    viewnum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    hot = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    pic = models.CharField(max_length=120)
    picflag = models.IntegerField()
    noreply = models.IntegerField()
    friend = models.IntegerField()
    password = models.CharField(max_length=10)
    click_1 = models.PositiveSmallIntegerField()
    click_2 = models.PositiveSmallIntegerField()
    click_3 = models.PositiveSmallIntegerField()
    click_4 = models.PositiveSmallIntegerField()
    click_5 = models.PositiveSmallIntegerField()
    fromdevice = models.CharField(max_length=50, blank=True, null=True)
    attachid = models.SmallIntegerField(blank=True, null=True)
    attachpath = models.CharField(max_length=120, blank=True, null=True)
    attachname = models.CharField(max_length=120, blank=True, null=True)
    attachsize = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_blog'


class IhomeBlogfield(models.Model):
    blogid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    tag = models.CharField(max_length=255)
    message = models.TextField()
    postip = models.CharField(max_length=20)
    related = models.TextField()
    relatedtime = models.PositiveIntegerField()
    target_ids = models.TextField()
    hotuser = models.TextField()
    magiccolor = models.IntegerField()
    magicpaper = models.IntegerField()
    magiccall = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_blogfield'


class IhomeCache(models.Model):
    cachekey = models.CharField(primary_key=True, max_length=16)
    value = models.TextField()
    mtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_cache'


class IhomeCalendar(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    calendar_name = models.CharField(max_length=100, blank=True, null=True)
    dateline = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_calendar'


class IhomeCalendarInfo(models.Model):
    calendar_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    start_t = models.IntegerField(blank=True, null=True)
    end_t = models.IntegerField(blank=True, null=True)
    bgcolor = models.CharField(max_length=18, blank=True, null=True)
    is_send_msg = models.IntegerField(blank=True, null=True)
    dateline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_calendar_info'


class IhomeClass(models.Model):
    classid = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=40)
    uid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_class'


class IhomeClick(models.Model):
    clickid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    idtype = models.CharField(max_length=15)
    displayorder = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_click'


class IhomeClickuser(models.Model):
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=15)
    clickid = models.PositiveSmallIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_clickuser'


class IhomeColumntable(models.Model):
    chart_tag = models.CharField(max_length=50)
    xaxis_tag = models.CharField(max_length=20)
    value = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ihome_columntable'


class IhomeComment(models.Model):
    cid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=20)
    authorid = models.PositiveIntegerField()
    author = models.CharField(max_length=15)
    ip = models.CharField(max_length=20)
    dateline = models.PositiveIntegerField()
    message = models.TextField()
    magicflicker = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_comment'


class IhomeComplain(models.Model):
    doid = models.IntegerField()
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    atuid = models.IntegerField()
    atuname = models.CharField(max_length=100)
    isreply = models.IntegerField()
    addtime = models.IntegerField()
    dateline = models.IntegerField()
    replytime = models.IntegerField()
    expire = models.IntegerField()
    times = models.IntegerField()
    atdepartment = models.CharField(max_length=255)
    atdeptuid = models.IntegerField()
    issendmsg = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    datatime = models.CharField(max_length=45, blank=True, null=True)
    ontrack = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    curuid = models.IntegerField(blank=True, null=True)
    curusername = models.CharField(max_length=20, blank=True, null=True)
    relay_times = models.IntegerField(blank=True, null=True)
    relayed_by = models.CharField(max_length=40, blank=True, null=True)
    lastopid = models.PositiveIntegerField(blank=True, null=True)
    locked = models.IntegerField(blank=True, null=True)
    complain_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_complain'


class IhomeComplainDep(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    upnum = models.PositiveIntegerField()
    downnum = models.PositiveIntegerField()
    updownnum = models.PositiveIntegerField()
    allreplynum = models.PositiveIntegerField()
    allreplysecs = models.PositiveIntegerField()
    score = models.IntegerField()
    aversecs = models.PositiveIntegerField()
    lastupdate = models.PositiveIntegerField()
    depduty = models.CharField(max_length=200)
    telephone = models.CharField(max_length=16)
    office = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ihome_complain_dep'


class IhomeComplainDepRank(models.Model):
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=20)
    upnum = models.PositiveIntegerField()
    downnum = models.PositiveIntegerField()
    updownnum = models.PositiveIntegerField()
    complainnum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    replysecs = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_complain_dep_rank'


class IhomeComplainOp(models.Model):
    doid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=20)
    message = models.TextField()
    optype = models.PositiveSmallIntegerField()
    dateline = models.PositiveIntegerField()
    upnum = models.PositiveIntegerField()
    downnum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    opvalue = models.CharField(max_length=20)
    curusername = models.CharField(max_length=20, blank=True, null=True)
    finish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_complain_op'


class IhomeComplainOpUpdown(models.Model):
    opid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    updown = models.IntegerField()
    username = models.CharField(max_length=20)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_complain_op_updown'
        unique_together = (('opid', 'uid', 'updown'),)


class IhomeComplainResp(models.Model):
    uid = models.PositiveIntegerField()
    doid = models.PositiveIntegerField()
    opid = models.PositiveIntegerField()
    replysecs = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_complain_resp'


class IhomeComplainTagcloud(models.Model):
    tag_word = models.CharField(max_length=20)
    tag_count = models.IntegerField()
    max_type = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    datatime = models.CharField(max_length=45, blank=True, null=True)
    atuid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_complain_tagcloud'


class IhomeComplainUid(models.Model):
    uid = models.IntegerField()
    foruid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_complain_uid'


class IhomeConfig(models.Model):
    var = models.CharField(primary_key=True, max_length=30)
    datavalue = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_config'


class IhomeCourse(models.Model):
    courseid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    day = models.CharField(max_length=10)
    times = models.IntegerField()
    timef = models.IntegerField()
    coursename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ihome_course'


class IhomeCreditlog(models.Model):
    clid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    cyclenum = models.PositiveIntegerField()
    credit = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    starttime = models.PositiveIntegerField()
    info = models.TextField()
    user = models.TextField()
    app = models.TextField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_creditlog'


class IhomeCreditrule(models.Model):
    rid = models.AutoField(primary_key=True)
    rulename = models.CharField(max_length=20)
    action = models.CharField(max_length=20)
    cycletype = models.IntegerField()
    cycletime = models.IntegerField()
    rewardnum = models.IntegerField()
    rewardtype = models.IntegerField()
    norepeat = models.IntegerField()
    credit = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_creditrule'


class IhomeCron(models.Model):
    cronid = models.PositiveSmallIntegerField(primary_key=True)
    available = models.IntegerField()
    type = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)
    lastrun = models.PositiveIntegerField()
    nextrun = models.PositiveIntegerField()
    weekday = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'ihome_cron'


class IhomeData(models.Model):
    var = models.CharField(primary_key=True, max_length=20)
    datavalue = models.TextField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_data'


class IhomeDeveloper(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ihome_developer'


class IhomeDocomment(models.Model):
    upid = models.PositiveIntegerField()
    doid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    message = models.TextField()
    ip = models.CharField(max_length=20)
    grade = models.PositiveSmallIntegerField()
    complainborn = models.IntegerField(db_column='complainBorn')  # Field name made lowercase.
    complainopid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_docomment'


class IhomeDoing(models.Model):
    doid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    from_field = models.CharField(db_column='from', max_length=20)  # Field renamed because it was a Python reserved word.
    dateline = models.PositiveIntegerField()
    message = models.TextField()
    ip = models.CharField(max_length=20)
    replynum = models.PositiveIntegerField()
    mood = models.SmallIntegerField()
    fromdevice = models.CharField(max_length=50, blank=True, null=True)
    image_1 = models.CharField(max_length=255, blank=True, null=True)
    image_1_link = models.CharField(max_length=255, blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_doing'


class IhomeEmailinvite(models.Model):
    uid = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    already_invite = models.IntegerField(blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    startyear = models.CharField(max_length=20, blank=True, null=True)
    academy = models.CharField(max_length=20, blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    md5 = models.CharField(max_length=50, blank=True, null=True)
    var = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_emailinvite'


class IhomeEvent(models.Model):
    eventid = models.AutoField(primary_key=True)
    topicid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    title = models.CharField(max_length=80)
    classid = models.PositiveSmallIntegerField()
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    location = models.CharField(max_length=80)
    poster = models.CharField(max_length=60)
    thumb = models.IntegerField()
    remote = models.IntegerField()
    deadline = models.PositiveIntegerField()
    starttime = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()
    public = models.IntegerField()
    membernum = models.PositiveIntegerField()
    follownum = models.PositiveIntegerField()
    viewnum = models.PositiveIntegerField()
    grade = models.IntegerField()
    recommendtime = models.PositiveIntegerField()
    tagid = models.PositiveIntegerField()
    picnum = models.PositiveIntegerField()
    threadnum = models.PositiveIntegerField()
    updatetime = models.PositiveIntegerField()
    hot = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_event'


class IhomeEventclass(models.Model):
    classid = models.PositiveSmallIntegerField(primary_key=True)
    classname = models.CharField(unique=True, max_length=80)
    poster = models.IntegerField()
    template = models.TextField()
    displayorder = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_eventclass'


class IhomeEventfield(models.Model):
    eventid = models.AutoField(primary_key=True)
    detail = models.TextField()
    template = models.CharField(max_length=255)
    limitnum = models.PositiveIntegerField()
    verify = models.IntegerField()
    allowpic = models.IntegerField()
    allowpost = models.IntegerField()
    allowinvite = models.IntegerField()
    allowfellow = models.IntegerField()
    hotuser = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_eventfield'


class IhomeEventinvite(models.Model):
    eventid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    touid = models.PositiveIntegerField()
    tousername = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_eventinvite'
        unique_together = (('eventid', 'touid'),)


class IhomeEventpic(models.Model):
    picid = models.PositiveIntegerField(primary_key=True)
    eventid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_eventpic'


class IhomeExchangeperson(models.Model):
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    longid = models.CharField(max_length=30, blank=True, null=True)
    realname = models.CharField(max_length=30, blank=True, null=True)
    identifier = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=30, blank=True, null=True)
    ethnic = models.CharField(max_length=20, blank=True, null=True)
    birthprovince = models.CharField(max_length=100, blank=True, null=True)
    sourcearea = models.CharField(max_length=20, blank=True, null=True)
    sourceschool = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    startyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    unit = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    dateline = models.DateTimeField(blank=True, null=True)
    admissionid = models.IntegerField(blank=True, null=True)
    candidateid = models.CharField(max_length=20, blank=True, null=True)
    bhid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_exchangeperson'


class IhomeFeed(models.Model):
    feedid = models.AutoField(primary_key=True)
    appid = models.PositiveSmallIntegerField()
    icon = models.CharField(max_length=30)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    friend = models.IntegerField()
    hash_template = models.CharField(max_length=32)
    hash_data = models.CharField(max_length=32)
    title_template = models.TextField()
    title_data = models.TextField()
    body_template = models.TextField()
    body_data = models.TextField()
    body_general = models.TextField()
    image_1 = models.CharField(max_length=255)
    image_1_link = models.CharField(max_length=255)
    image_2 = models.CharField(max_length=255)
    image_2_link = models.CharField(max_length=255)
    image_3 = models.CharField(max_length=255)
    image_3_link = models.CharField(max_length=255)
    image_4 = models.CharField(max_length=255)
    image_4_link = models.CharField(max_length=255)
    target_ids = models.TextField()
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=15)
    hot = models.PositiveIntegerField()
    fromdevice = models.CharField(max_length=50, blank=True, null=True)
    icontype = models.CharField(max_length=10, blank=True, null=True)
    upvotes = models.PositiveIntegerField()
    upvoters = models.TextField(blank=True, null=True)
    top = models.IntegerField()
    isdeleted = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_feed'


class IhomeForgiencreate(models.Model):
    username = models.CharField(max_length=45, blank=True, null=True)
    realname = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.CharField(max_length=45, blank=True, null=True)
    birth_year = models.CharField(max_length=45, blank=True, null=True)
    birth_month = models.CharField(max_length=45, blank=True, null=True)
    birth_day = models.CharField(max_length=45, blank=True, null=True)
    startyear = models.CharField(max_length=45, blank=True, null=True)
    academy = models.CharField(max_length=45, blank=True, null=True)
    ver = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    school = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_forgienCreate'


class IhomeFriend(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    fuid = models.PositiveIntegerField()
    fusername = models.CharField(max_length=15)
    status = models.IntegerField()
    gid = models.PositiveSmallIntegerField()
    note = models.CharField(max_length=50)
    num = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_friend'
        unique_together = (('uid', 'fuid'),)


class IhomeFriendTorecomment(models.Model):
    uid1 = models.IntegerField(blank=True, null=True)
    uid2 = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    res_torecomment = models.CharField(db_column='res_toRecomment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_friend_toRecomment'


class IhomeFriendguide(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    fuid = models.PositiveIntegerField()
    fusername = models.CharField(max_length=15)
    num = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_friendguide'
        unique_together = (('uid', 'fuid'),)


class IhomeFriendlog(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    fuid = models.PositiveIntegerField()
    action = models.CharField(max_length=10)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_friendlog'
        unique_together = (('uid', 'fuid'),)


class IhomeGrantinvite(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    public_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_grantinvite'


class IhomeIntranetip(models.Model):
    ip = models.CharField(max_length=20, blank=True, null=True)
    mask = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_intranetip'


class IhomeInvite(models.Model):
    uid = models.PositiveIntegerField()
    code = models.CharField(max_length=20)
    fuid = models.PositiveIntegerField()
    fusername = models.CharField(max_length=15)
    type = models.IntegerField()
    email = models.CharField(max_length=100)
    appid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_invite'


class IhomeJifenCj(models.Model):
    lpid = models.IntegerField()
    total = models.SmallIntegerField()
    math = models.CharField(max_length=100)
    nums = models.IntegerField()
    getnums = models.IntegerField()
    sdate = models.IntegerField()
    edate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_jifen_cj'


class IhomeJifenCjlog(models.Model):
    uid = models.IntegerField()
    username = models.CharField(max_length=50)
    lpid = models.IntegerField()
    flag = models.IntegerField()
    time = models.IntegerField()
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ihome_jifen_cjlog'


class IhomeJifenDhlog(models.Model):
    uid = models.IntegerField()
    username = models.CharField(max_length=50)
    lpid = models.IntegerField()
    giftname = models.CharField(max_length=100)
    time = models.IntegerField()
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    get = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_jifen_dhlog'


class IhomeJifenLb(models.Model):
    name = models.CharField(max_length=50)
    nums = models.SmallIntegerField()
    des = models.CharField(max_length=1000)
    time = models.IntegerField()
    displayorder = models.IntegerField()
    pic = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ihome_jifen_lb'


class IhomeJifenLp(models.Model):
    lbid = models.IntegerField()
    name = models.CharField(max_length=50)
    total = models.SmallIntegerField()
    price = models.IntegerField()
    mprice = models.SmallIntegerField()
    des = models.TextField()
    score = models.IntegerField()
    pic = models.CharField(max_length=200)
    sdate = models.IntegerField()
    edate = models.IntegerField()
    time = models.IntegerField()
    views = models.SmallIntegerField()
    nums = models.SmallIntegerField()
    modders = models.SmallIntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_jifen_lp'


class IhomeJifenPl(models.Model):
    uid = models.IntegerField()
    username = models.CharField(max_length=50)
    lpid = models.IntegerField()
    score = models.IntegerField()
    content = models.TextField()
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_jifen_pl'


class IhomeJob(models.Model):
    title = models.CharField(max_length=100)
    viewcount = models.IntegerField()
    uid = models.IntegerField()
    type = models.IntegerField()
    createtime = models.DateTimeField()
    replynum = models.IntegerField()
    username = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ihome_job'


class IhomeJobContent3(models.Model):
    jobid = models.IntegerField()
    description = models.CharField(max_length=255)
    endtime = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_job_content_3'


class IhomeJobFav(models.Model):
    uid = models.IntegerField()
    jobid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_job_fav'


class IhomeLanguageHelpRequests(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    fuid = models.IntegerField(blank=True, null=True)
    dateline = models.CharField(max_length=45, blank=True, null=True)
    result = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_language_help_requests'


class IhomeLanguageUser(models.Model):
    uid = models.IntegerField(primary_key=True)
    knows = models.CharField(max_length=45, blank=True, null=True)
    want_to_know = models.CharField(max_length=45, blank=True, null=True)
    dateline = models.CharField(max_length=45, blank=True, null=True)
    fuid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_language_user'


class IhomeLivecount(models.Model):
    uid = models.PositiveIntegerField()
    timeline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_livecount'


class IhomeLog(models.Model):
    logid = models.AutoField(primary_key=True)
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ihome_log'


class IhomeLoginbg(models.Model):
    id = models.IntegerField(primary_key=True)
    bg_pic = models.CharField(max_length=50, blank=True, null=True)
    box_bg_col = models.CharField(max_length=10, blank=True, null=True)
    box_border_col = models.CharField(max_length=10, blank=True, null=True)
    btn_bg_col = models.CharField(max_length=10, blank=True, null=True)
    btn_border_col = models.CharField(max_length=10, blank=True, null=True)
    btn_font_col = models.CharField(max_length=10, blank=True, null=True)
    active_font_col = models.CharField(max_length=10, blank=True, null=True)
    back_font_col = models.CharField(max_length=10, blank=True, null=True)
    back_link_col = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_loginbg'


class IhomeLoginlog(models.Model):
    uid = models.IntegerField()
    logintime = models.IntegerField()
    ip = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_loginlog'


class IhomeMagic(models.Model):
    mid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=30)
    description = models.TextField()
    forbiddengid = models.TextField()
    charge = models.PositiveSmallIntegerField()
    experience = models.PositiveSmallIntegerField()
    provideperoid = models.PositiveIntegerField()
    providecount = models.PositiveSmallIntegerField()
    useperoid = models.PositiveIntegerField()
    usecount = models.PositiveSmallIntegerField()
    displayorder = models.PositiveSmallIntegerField()
    custom = models.TextField()
    close = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_magic'


class IhomeMagicinlog(models.Model):
    logid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    mid = models.CharField(max_length=15)
    count = models.PositiveSmallIntegerField()
    type = models.PositiveIntegerField()
    fromid = models.PositiveIntegerField()
    credit = models.PositiveSmallIntegerField()
    dateline = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_magicinlog'


class IhomeMagicstore(models.Model):
    mid = models.CharField(primary_key=True, max_length=15)
    storage = models.PositiveSmallIntegerField()
    lastprovide = models.PositiveIntegerField()
    sellcount = models.PositiveIntegerField()
    sellcredit = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_magicstore'


class IhomeMagicuselog(models.Model):
    logid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    mid = models.CharField(max_length=15)
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=20)
    count = models.PositiveIntegerField()
    data = models.TextField()
    dateline = models.PositiveIntegerField()
    expire = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_magicuselog'


class IhomeMailcron(models.Model):
    cid = models.AutoField(primary_key=True)
    touid = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    sendtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_mailcron'


class IhomeMailqueue(models.Model):
    qid = models.AutoField(primary_key=True)
    cid = models.PositiveIntegerField()
    subject = models.TextField()
    message = models.TextField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_mailqueue'


class IhomeMember(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'ihome_member'


class IhomeMobilegetpwd(models.Model):
    mobile = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    verifycode = models.CharField(max_length=6)
    dateline = models.PositiveIntegerField()
    ip = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_mobilegetpwd'


class IhomeMobileinvite(models.Model):
    uid = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    already_invite = models.IntegerField(blank=True, null=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    startyear = models.CharField(max_length=20, blank=True, null=True)
    academy = models.CharField(max_length=50, blank=True, null=True)
    var = models.CharField(max_length=8, blank=True, null=True)
    collegeid = models.CharField(max_length=30, blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_mobileinvite'


class IhomeMobilemsg(models.Model):
    msgid = models.AutoField(primary_key=True)
    issend = models.IntegerField()
    uid = models.IntegerField()
    tomobile = models.CharField(max_length=40)
    content = models.TextField()
    addtime = models.IntegerField()
    sendtime = models.CharField(max_length=15)
    atuname = models.CharField(max_length=30)
    num = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_mobilemsg'


class IhomeMobilereg(models.Model):
    mobile = models.CharField(max_length=15)
    realname = models.CharField(max_length=30)
    verifycode = models.CharField(max_length=6)
    dateline = models.PositiveIntegerField()
    ip = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_mobilereg'


class IhomeMtag(models.Model):
    tagid = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=40)
    fieldid = models.SmallIntegerField()
    membernum = models.PositiveIntegerField()
    threadnum = models.PositiveIntegerField()
    postnum = models.PositiveIntegerField()
    close = models.IntegerField()
    announcement = models.TextField()
    pic = models.CharField(max_length=150)
    closeapply = models.IntegerField()
    joinperm = models.IntegerField()
    viewperm = models.IntegerField()
    threadperm = models.IntegerField()
    postperm = models.IntegerField()
    recommend = models.IntegerField()
    moderator = models.CharField(max_length=255)
    startyear = models.CharField(max_length=8, blank=True, null=True)
    academy = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_mtag'


class IhomeMtaginvite(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    tagid = models.PositiveIntegerField()
    fromuid = models.PositiveIntegerField()
    fromusername = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_mtaginvite'
        unique_together = (('uid', 'tagid'),)


class IhomeMyapp(models.Model):
    appid = models.PositiveIntegerField(primary_key=True)
    appname = models.CharField(max_length=60)
    narrow = models.IntegerField()
    flag = models.IntegerField()
    version = models.PositiveIntegerField()
    displaymethod = models.IntegerField()
    displayorder = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_myapp'


class IhomeMyinvite(models.Model):
    typename = models.CharField(max_length=100)
    appid = models.IntegerField()
    type = models.IntegerField()
    fromuid = models.PositiveIntegerField()
    touid = models.PositiveIntegerField()
    myml = models.TextField()
    dateline = models.PositiveIntegerField()
    hash = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_myinvite'


class IhomeNoMtagRegister(models.Model):
    uid = models.IntegerField(primary_key=True)
    apply_uid = models.IntegerField(blank=True, null=True)
    apply_date = models.CharField(max_length=45, blank=True, null=True)
    pass_date = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_no_mtag_register'


class IhomeNotification(models.Model):
    uid = models.PositiveIntegerField()
    type = models.CharField(max_length=20)
    new = models.IntegerField()
    authorid = models.PositiveIntegerField()
    author = models.CharField(max_length=15)
    note = models.TextField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_notification'


class IhomeNtagUser(models.Model):
    tuid = models.AutoField(primary_key=True)
    tagid = models.IntegerField()
    uid = models.IntegerField()
    dotype = models.CharField(max_length=50)
    doid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_ntag_user'


class IhomeNtags(models.Model):
    tagid = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=128)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_ntags'


class IhomeParent(models.Model):
    uid = models.IntegerField()
    suid = models.IntegerField()
    isactive = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=30)
    realname = models.CharField(max_length=30, blank=True, null=True)
    job = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_parent'


class IhomePic(models.Model):
    picid = models.AutoField(primary_key=True)
    albumid = models.PositiveIntegerField()
    topicid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    postip = models.CharField(max_length=20)
    filename = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    size = models.PositiveIntegerField()
    filepath = models.CharField(max_length=60)
    thumb = models.IntegerField()
    remote = models.IntegerField()
    hot = models.PositiveIntegerField()
    click_6 = models.PositiveSmallIntegerField()
    click_7 = models.PositiveSmallIntegerField()
    click_8 = models.PositiveSmallIntegerField()
    click_9 = models.PositiveSmallIntegerField()
    click_10 = models.PositiveSmallIntegerField()
    magicframe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_pic'


class IhomePicfield(models.Model):
    picid = models.PositiveIntegerField(primary_key=True)
    hotuser = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_picfield'


class IhomePietable(models.Model):
    chart_tag = models.CharField(max_length=50)
    item_tag = models.CharField(max_length=20)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_pietable'


class IhomePoke(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    fromuid = models.PositiveIntegerField()
    fromusername = models.CharField(max_length=15)
    note = models.CharField(max_length=255)
    dateline = models.PositiveIntegerField()
    iconid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_poke'
        unique_together = (('uid', 'fromuid'),)


class IhomePoll(models.Model):
    pid = models.AutoField(primary_key=True)
    topicid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    subject = models.CharField(max_length=80)
    voternum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    multiple = models.IntegerField()
    maxchoice = models.IntegerField()
    minchoice = models.IntegerField()
    sex = models.IntegerField()
    anonymous = models.IntegerField()
    noreply = models.IntegerField()
    credit = models.PositiveIntegerField()
    percredit = models.PositiveIntegerField()
    expiration = models.PositiveIntegerField()
    lastvote = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    hot = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_poll'


class IhomePollfield(models.Model):
    pid = models.PositiveIntegerField(primary_key=True)
    notify = models.IntegerField()
    message = models.TextField()
    summary = models.TextField()
    option = models.TextField()
    invite = models.TextField()
    hotuser = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_pollfield'


class IhomePolloption(models.Model):
    oid = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField()
    votenum = models.PositiveIntegerField()
    option = models.CharField(max_length=200)
    link = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_polloption'


class IhomePolluser(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    pid = models.PositiveIntegerField()
    option = models.TextField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_polluser'
        unique_together = (('uid', 'pid'),)


class IhomePost(models.Model):
    pid = models.AutoField(primary_key=True)
    tagid = models.PositiveIntegerField()
    tid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    ip = models.CharField(max_length=20)
    dateline = models.PositiveIntegerField()
    message = models.TextField()
    pic = models.CharField(max_length=255)
    isthread = models.IntegerField()
    hotuser = models.TextField()
    anonymous = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_post'


class IhomePowerlevel(models.Model):
    pid = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100)
    dept_uid = models.IntegerField()
    isdept = models.IntegerField()
    up_uid = models.CharField(max_length=40)
    official = models.CharField(max_length=100)
    mobile = models.CharField(max_length=40, blank=True, null=True)
    depduty = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=16)
    office = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ihome_powerlevel'


class IhomePrize(models.Model):
    tel = models.CharField(max_length=11)
    sid = models.CharField(max_length=20)
    prize = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_prize'
        unique_together = (('id', 'sid', 'tel'),)


class IhomePrizeip(models.Model):
    tel = models.CharField(max_length=11)
    sid = models.CharField(max_length=20)
    prize = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_prizeip'
        unique_together = (('id', 'sid', 'tel'),)


class IhomeProfield(models.Model):
    fieldid = models.PositiveSmallIntegerField(primary_key=True)
    title = models.CharField(max_length=80)
    note = models.CharField(max_length=255)
    formtype = models.CharField(max_length=20)
    inputnum = models.PositiveSmallIntegerField()
    choice = models.TextField()
    mtagminnum = models.PositiveSmallIntegerField()
    manualmoderator = models.IntegerField()
    manualmember = models.IntegerField()
    displayorder = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_profield'


class IhomeProfilefield(models.Model):
    fieldid = models.PositiveSmallIntegerField(primary_key=True)
    title = models.CharField(max_length=80)
    note = models.CharField(max_length=255)
    formtype = models.CharField(max_length=20)
    maxsize = models.PositiveIntegerField()
    required = models.IntegerField()
    invisible = models.IntegerField()
    allowsearch = models.IntegerField()
    choice = models.TextField()
    displayorder = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_profilefield'


class IhomeProtectInfo(models.Model):
    uid = models.IntegerField(primary_key=True)
    question1 = models.CharField(max_length=400)
    answer1 = models.CharField(max_length=400)
    question2 = models.CharField(max_length=400)
    answer2 = models.CharField(max_length=400)
    question3 = models.CharField(max_length=400)
    answer3 = models.CharField(max_length=400)
    question1_1 = models.CharField(max_length=400)
    answer1_1 = models.CharField(max_length=400)
    question2_1 = models.CharField(max_length=400)
    answer2_1 = models.CharField(max_length=400)
    question3_1 = models.CharField(max_length=400)
    answer3_1 = models.CharField(max_length=400)
    mobile = models.CharField(max_length=20)
    mobile_1 = models.CharField(max_length=20)
    mobile_code = models.CharField(max_length=20)
    mobile_send_time = models.IntegerField()
    email = models.CharField(max_length=20)
    email_1 = models.CharField(max_length=20)
    email_code = models.CharField(max_length=20)
    mobile_send_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_protect_info'


class IhomeProxy(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    menu_0 = models.IntegerField()
    menu_1 = models.IntegerField()
    menu_2 = models.IntegerField()
    menu_3 = models.IntegerField()
    menu_4 = models.IntegerField()
    menu_5 = models.IntegerField()
    extra = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_proxy'


class IhomePubcomment(models.Model):
    pub_uid = models.IntegerField()
    pub_name = models.CharField(max_length=60, blank=True, null=True)
    uid = models.IntegerField()
    username = models.CharField(max_length=30, blank=True, null=True)
    totality_grade = models.IntegerField()
    totality_comment = models.CharField(max_length=255, blank=True, null=True)
    message_grade = models.IntegerField()
    message_comment = models.CharField(max_length=255, blank=True, null=True)
    speed_grade = models.IntegerField()
    speed_comment = models.CharField(max_length=255, blank=True, null=True)
    quality_grade = models.IntegerField()
    quality_comment = models.CharField(max_length=255, blank=True, null=True)
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_pubcomment'


class IhomePublicapply(models.Model):
    appid = models.AutoField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    reason = models.TextField()
    email = models.CharField(max_length=100)
    adminuid = models.IntegerField(blank=True, null=True)
    ruthed = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    contactid = models.CharField(max_length=10)
    pw = models.CharField(max_length=10)
    apptime = models.CharField(max_length=20)
    type = models.IntegerField()
    appuid = models.IntegerField()
    flink = models.CharField(max_length=999, blank=True, null=True)
    adminupdatetime = models.CharField(max_length=20, blank=True, null=True)
    nameupdatetime = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_publicapply'


class IhomePublicflink(models.Model):
    uid = models.IntegerField(primary_key=True)
    flink = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_publicflink'


class IhomeQprize(models.Model):
    tel = models.CharField(max_length=11)
    sid = models.CharField(max_length=20)
    prize = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    pri = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_qprize'
        unique_together = (('id', 'sid', 'tel'),)


class IhomeQprizeNew(models.Model):
    tel = models.CharField(max_length=11)
    sid = models.CharField(max_length=20)
    prize = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    pri = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_qprize_new'
        unique_together = (('id', 'sid', 'tel'),)


class IhomeQprizeip(models.Model):
    tel = models.CharField(max_length=11)
    sid = models.CharField(max_length=20)
    prize = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    timeline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_qprizeip'
        unique_together = (('id', 'sid', 'tel'),)


class IhomeRecPublic(models.Model):
    id = models.IntegerField()
    uid = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    addtime = models.CharField(max_length=45, blank=True, null=True)
    add_reason = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_rec_public'


class IhomeRecommendation(models.Model):
    feedid = models.AutoField(primary_key=True)
    appid = models.PositiveSmallIntegerField()
    icon = models.CharField(max_length=30)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    friend = models.IntegerField()
    hash_template = models.CharField(max_length=32)
    hash_data = models.CharField(max_length=32)
    title_template = models.TextField()
    title_data = models.TextField()
    body_template = models.TextField()
    body_data = models.TextField()
    body_general = models.TextField()
    image_1 = models.CharField(max_length=255)
    image_1_link = models.CharField(max_length=255)
    image_2 = models.CharField(max_length=255)
    image_2_link = models.CharField(max_length=255)
    image_3 = models.CharField(max_length=255)
    image_3_link = models.CharField(max_length=255)
    image_4 = models.CharField(max_length=255)
    image_4_link = models.CharField(max_length=255)
    target_ids = models.TextField()
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=15)
    hot = models.PositiveIntegerField()
    fromdevice = models.CharField(max_length=50, blank=True, null=True)
    icontype = models.CharField(max_length=10, blank=True, null=True)
    recfrom_i = models.IntegerField()
    weight = models.PositiveIntegerField()
    score = models.FloatField()
    autorec = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_recommendation'


class IhomeRegisterAnalyse(models.Model):
    user_type = models.CharField(max_length=20)
    all_num = models.IntegerField()
    register_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_register_analyse'


class IhomeReport(models.Model):
    rid = models.AutoField(primary_key=True)
    id = models.PositiveIntegerField()
    idtype = models.CharField(max_length=15)
    new = models.IntegerField()
    num = models.PositiveSmallIntegerField()
    dateline = models.PositiveIntegerField()
    reason = models.TextField()
    uids = models.TextField()
    rtype = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_report'


class IhomeSession(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=32)
    lastactivity = models.PositiveIntegerField()
    ip = models.PositiveIntegerField()
    magichidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_session'


class IhomeShare(models.Model):
    sid = models.AutoField(primary_key=True)
    topicid = models.PositiveIntegerField()
    type = models.CharField(max_length=30)
    id = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    title_template = models.TextField()
    body_template = models.TextField()
    body_data = models.TextField()
    body_general = models.TextField()
    image = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    hot = models.PositiveIntegerField()
    hotuser = models.TextField()
    fromdevice = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_share'


class IhomeShow(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    credit = models.PositiveIntegerField()
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ihome_show'


class IhomeSignupAnalyse(models.Model):
    usertype = models.CharField(max_length=20)
    total = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_signup_analyse'


class IhomeSignupLog(models.Model):
    uid = models.IntegerField()
    usertype = models.CharField(max_length=20)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ihome_signup_log'


class IhomeSms(models.Model):
    smsid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    username = models.CharField(max_length=30)
    sendnum = models.CharField(max_length=15)
    message = models.CharField(max_length=280)
    postip = models.CharField(max_length=64)
    dateline = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_sms'


class IhomeSoftware(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    pic = models.CharField(max_length=100, blank=True, null=True)
    nums = models.SmallIntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    modders = models.IntegerField(blank=True, null=True)
    des = models.TextField(blank=True, null=True)
    sdate = models.IntegerField(blank=True, null=True)
    edate = models.IntegerField(blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_software'


class IhomeSoftwareComment(models.Model):
    comid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    sid = models.PositiveIntegerField()
    ip = models.CharField(max_length=15)
    score = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    stamptime = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ihome_software_comment'


class IhomeSoftwareDownload(models.Model):
    downid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    sid = models.PositiveIntegerField()
    ip = models.CharField(max_length=15)
    stamptime = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ihome_software_download'


class IhomeSpace(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    groupid = models.PositiveSmallIntegerField()
    credit = models.IntegerField()
    experience = models.IntegerField()
    username = models.CharField(max_length=15)
    name = models.CharField(max_length=50, blank=True, null=True)
    namestatus = models.IntegerField()
    videostatus = models.IntegerField()
    domain = models.CharField(max_length=15)
    friendnum = models.PositiveIntegerField()
    viewnum = models.PositiveIntegerField()
    notenum = models.PositiveIntegerField()
    addfriendnum = models.PositiveSmallIntegerField()
    mtaginvitenum = models.PositiveSmallIntegerField()
    eventinvitenum = models.PositiveSmallIntegerField()
    myinvitenum = models.PositiveSmallIntegerField()
    pokenum = models.PositiveSmallIntegerField()
    doingnum = models.PositiveSmallIntegerField()
    blognum = models.PositiveSmallIntegerField()
    albumnum = models.PositiveSmallIntegerField()
    threadnum = models.PositiveSmallIntegerField()
    pollnum = models.PositiveSmallIntegerField()
    eventnum = models.PositiveSmallIntegerField()
    sharenum = models.PositiveSmallIntegerField()
    dateline = models.PositiveIntegerField()
    updatetime = models.PositiveIntegerField()
    lastsearch = models.PositiveIntegerField()
    lastpost = models.PositiveIntegerField()
    lastlogin = models.PositiveIntegerField()
    lastsend = models.PositiveIntegerField()
    attachsize = models.PositiveIntegerField()
    addsize = models.PositiveIntegerField()
    addfriend = models.PositiveSmallIntegerField()
    flag = models.IntegerField()
    newpm = models.PositiveSmallIntegerField()
    avatar = models.IntegerField()
    regip = models.CharField(max_length=15)
    ip = models.PositiveIntegerField()
    mood = models.PositiveSmallIntegerField()
    audnum = models.IntegerField()
    aud = models.TextField(blank=True, null=True)
    pptype = models.IntegerField()
    ppnum = models.IntegerField()
    pass_msg = models.CharField(max_length=64, blank=True, null=True)
    caninvite = models.IntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=10, blank=True, null=True)
    invite_remain = models.IntegerField()
    consul = models.CharField(max_length=45, blank=True, null=True)
    overseas_tip = models.CharField(max_length=45, blank=True, null=True)
    asstconsul = models.CharField(db_column='asstConsul', max_length=10, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(max_length=16)
    office = models.CharField(max_length=100)
    depduty = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=30, blank=True, null=True)
    identity = models.CharField(max_length=30, blank=True, null=True)
    iden_t = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_space'


class IhomeSpacefield(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    realname = models.CharField(max_length=50, blank=True, null=True)
    realbirth = models.CharField(max_length=10, blank=True, null=True)
    sex = models.IntegerField()
    email = models.CharField(max_length=100)
    newemail = models.CharField(max_length=100)
    emailcheck = models.IntegerField()
    mobile = models.CharField(max_length=40)
    verifycode = models.CharField(max_length=6)
    mobiletask = models.IntegerField()
    qq = models.CharField(max_length=20)
    msn = models.CharField(max_length=80)
    msnrobot = models.CharField(max_length=15)
    msncstatus = models.IntegerField()
    videopic = models.CharField(max_length=32)
    birthyear = models.PositiveSmallIntegerField()
    birthmonth = models.PositiveIntegerField()
    birthday = models.PositiveIntegerField()
    blood = models.CharField(max_length=5)
    marry = models.IntegerField()
    birthprovince = models.CharField(max_length=20)
    birthcity = models.CharField(max_length=20)
    resideprovince = models.CharField(max_length=20)
    residecity = models.CharField(max_length=20)
    note = models.TextField()
    spacenote = models.TextField()
    authstr = models.CharField(max_length=20)
    theme = models.CharField(max_length=20)
    nocss = models.IntegerField()
    menunum = models.PositiveSmallIntegerField()
    css = models.TextField()
    privacy = models.TextField()
    friend = models.TextField()
    feedfriend = models.TextField()
    sendmail = models.TextField()
    magicstar = models.IntegerField()
    magicexpire = models.PositiveIntegerField()
    timeoffset = models.CharField(max_length=20)
    defaultemail = models.CharField(max_length=100, blank=True, null=True)
    diy_bg = models.CharField(max_length=255, blank=True, null=True)
    diy_bg_style = models.IntegerField(blank=True, null=True)
    diy_colors = models.IntegerField(blank=True, null=True)
    diy_bg_enabled = models.IntegerField(blank=True, null=True)
    diy_alpha = models.CharField(max_length=4, blank=True, null=True)
    index_bg = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=32, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=32, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'ihome_spacefield'


class IhomeSpaceforeign(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=20, blank=True, null=True)
    lat = models.CharField(max_length=20, blank=True, null=True)
    cer = models.CharField(max_length=45)
    dataline = models.CharField(max_length=45, blank=True, null=True)
    passline = models.CharField(max_length=45, blank=True, null=True)
    pass_uid = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_spaceforeign'


class IhomeSpaceinfo(models.Model):
    infoid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    type = models.CharField(max_length=20)
    subtype = models.CharField(max_length=20)
    title = models.TextField()
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    friend = models.IntegerField()
    startyear = models.PositiveSmallIntegerField()
    endyear = models.PositiveSmallIntegerField()
    startmonth = models.PositiveSmallIntegerField()
    endmonth = models.PositiveSmallIntegerField()
    subtitle = models.TextField()
    class_field = models.CharField(db_column='class', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'ihome_spaceinfo'


class IhomeSpacelog(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    opuid = models.PositiveIntegerField()
    opusername = models.CharField(max_length=15)
    flag = models.IntegerField()
    expiration = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_spacelog'


class IhomeStat(models.Model):
    daytime = models.PositiveIntegerField(primary_key=True)
    login = models.PositiveSmallIntegerField()
    register = models.PositiveSmallIntegerField()
    invite = models.PositiveSmallIntegerField()
    appinvite = models.PositiveSmallIntegerField()
    doing = models.PositiveSmallIntegerField()
    blog = models.PositiveSmallIntegerField()
    pic = models.PositiveSmallIntegerField()
    video = models.SmallIntegerField()
    poll = models.PositiveSmallIntegerField()
    event = models.PositiveSmallIntegerField()
    share = models.PositiveSmallIntegerField()
    thread = models.PositiveSmallIntegerField()
    docomment = models.PositiveSmallIntegerField()
    blogcomment = models.PositiveSmallIntegerField()
    videocomment = models.SmallIntegerField()
    piccomment = models.PositiveSmallIntegerField()
    pollcomment = models.PositiveSmallIntegerField()
    pollvote = models.PositiveSmallIntegerField()
    eventcomment = models.PositiveSmallIntegerField()
    eventjoin = models.PositiveSmallIntegerField()
    sharecomment = models.PositiveSmallIntegerField()
    post = models.PositiveSmallIntegerField()
    wall = models.PositiveSmallIntegerField()
    poke = models.PositiveSmallIntegerField()
    click = models.PositiveSmallIntegerField()
    videoshare = models.SmallIntegerField()
    attach = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_stat'


class IhomeStatuser(models.Model):
    uid = models.PositiveIntegerField()
    daytime = models.PositiveIntegerField()
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ihome_statuser'


class IhomeStuemp(models.Model):
    collegeid = models.CharField(primary_key=True, max_length=32)
    unit = models.CharField(max_length=128)
    city_code = models.IntegerField()
    province_city = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'ihome_stuemp'


class IhomeTag(models.Model):
    tagid = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=30)
    uid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    blognum = models.PositiveSmallIntegerField()
    close = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_tag'


class IhomeTagblog(models.Model):
    tagid = models.PositiveIntegerField(primary_key=True)
    blogid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_tagblog'
        unique_together = (('tagid', 'blogid'),)


class IhomeTagcloud(models.Model):
    tag_word = models.CharField(max_length=20)
    tag_count = models.IntegerField()
    max_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_tagcloud'


class IhomeTagspace(models.Model):
    tagid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    grade = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_tagspace'
        unique_together = (('tagid', 'uid'),)


class IhomeTask(models.Model):
    taskid = models.PositiveSmallIntegerField(primary_key=True)
    available = models.IntegerField()
    name = models.CharField(max_length=50)
    note = models.TextField()
    num = models.PositiveIntegerField()
    maxnum = models.PositiveIntegerField()
    image = models.CharField(max_length=150)
    filename = models.CharField(max_length=50)
    starttime = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()
    nexttime = models.PositiveIntegerField()
    nexttype = models.CharField(max_length=20)
    credit = models.SmallIntegerField()
    displayorder = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_task'


class IhomeThread(models.Model):
    tid = models.AutoField(primary_key=True)
    topicid = models.PositiveIntegerField()
    tagid = models.PositiveIntegerField()
    eventid = models.PositiveIntegerField()
    subject = models.CharField(max_length=80)
    magiccolor = models.PositiveIntegerField()
    magicegg = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    viewnum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    lastpost = models.PositiveIntegerField()
    lastauthor = models.CharField(max_length=15)
    lastauthorid = models.PositiveIntegerField()
    displayorder = models.PositiveIntegerField()
    digest = models.IntegerField()
    hot = models.PositiveIntegerField()
    click_11 = models.PositiveSmallIntegerField()
    click_12 = models.PositiveSmallIntegerField()
    click_13 = models.PositiveSmallIntegerField()
    click_14 = models.PositiveSmallIntegerField()
    click_15 = models.PositiveSmallIntegerField()
    fromdevice = models.CharField(max_length=50, blank=True, null=True)
    solved = models.IntegerField()
    anonymous = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_thread'


class IhomeTopic(models.Model):
    topicid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    subject = models.CharField(max_length=80)
    message = models.TextField()
    jointype = models.CharField(max_length=255)
    joingid = models.CharField(max_length=255)
    pic = models.CharField(max_length=100)
    thumb = models.IntegerField()
    remote = models.IntegerField()
    joinnum = models.PositiveIntegerField()
    lastpost = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_topic'


class IhomeTopicuser(models.Model):
    uid = models.PositiveIntegerField()
    topicid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_topicuser'


class IhomeTreecomments(models.Model):
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=20)
    rootid = models.CharField(max_length=20)
    message = models.TextField()
    dateline = models.PositiveIntegerField()
    upid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_treecomments'


class IhomeUncheckarrangement(models.Model):
    arrangementid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    classid = models.PositiveSmallIntegerField()
    starttime = models.PositiveIntegerField(unique=True)
    message = models.TextField()
    tag = models.CharField(max_length=255)
    postip = models.CharField(max_length=20)
    viewnum = models.PositiveIntegerField()
    replynum = models.PositiveIntegerField()
    dateline = models.IntegerField()
    pic = models.CharField(max_length=120)
    picflag = models.IntegerField()
    noreply = models.IntegerField()
    click_1 = models.SmallIntegerField()
    click_2 = models.SmallIntegerField()
    click_3 = models.SmallIntegerField()
    click_4 = models.SmallIntegerField()
    click_5 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_unCheckArrangement'


class IhomeUserapp(models.Model):
    uid = models.PositiveIntegerField()
    appid = models.PositiveIntegerField()
    appname = models.CharField(max_length=60)
    privacy = models.IntegerField()
    allowsidenav = models.IntegerField()
    allowfeed = models.IntegerField()
    allowprofilelink = models.IntegerField()
    narrow = models.IntegerField()
    menuorder = models.SmallIntegerField()
    displayorder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_userapp'


class IhomeUserappfield(models.Model):
    uid = models.PositiveIntegerField()
    appid = models.PositiveIntegerField()
    profilelink = models.TextField()
    myml = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihome_userappfield'


class IhomeUserevent(models.Model):
    eventid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    status = models.IntegerField()
    fellow = models.PositiveIntegerField()
    template = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ihome_userevent'
        unique_together = (('eventid', 'uid'),)


class IhomeUsergroup(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    grouptitle = models.CharField(max_length=20)
    system = models.IntegerField()
    banvisit = models.IntegerField()
    explower = models.IntegerField()
    maxfriendnum = models.PositiveSmallIntegerField()
    maxattachsize = models.PositiveIntegerField()
    allowhtml = models.IntegerField()
    allowcomment = models.IntegerField()
    searchinterval = models.PositiveSmallIntegerField()
    searchignore = models.IntegerField()
    postinterval = models.PositiveSmallIntegerField()
    spamignore = models.IntegerField()
    videophotoignore = models.IntegerField()
    allowblog = models.IntegerField()
    allowdoing = models.IntegerField()
    allowupload = models.IntegerField()
    allowshare = models.IntegerField()
    allowmtag = models.IntegerField()
    allowthread = models.IntegerField()
    allowpost = models.IntegerField()
    allowcss = models.IntegerField()
    allowpoke = models.IntegerField()
    allowfriend = models.IntegerField()
    allowpoll = models.IntegerField()
    allowclick = models.IntegerField()
    allowevent = models.IntegerField()
    allowmagic = models.IntegerField()
    allowpm = models.IntegerField()
    allowviewvideopic = models.IntegerField()
    allowmyop = models.IntegerField()
    allowtopic = models.IntegerField()
    allowstat = models.IntegerField()
    magicdiscount = models.IntegerField()
    verifyevent = models.IntegerField()
    edittrail = models.IntegerField()
    domainlength = models.PositiveSmallIntegerField()
    closeignore = models.IntegerField()
    seccode = models.IntegerField()
    color = models.CharField(max_length=10)
    icon = models.CharField(max_length=100)
    manageconfig = models.IntegerField()
    managenetwork = models.IntegerField()
    manageprofilefield = models.IntegerField()
    manageprofield = models.IntegerField()
    manageusergroup = models.IntegerField()
    managefeed = models.IntegerField()
    manageshare = models.IntegerField()
    managedoing = models.IntegerField()
    manageblog = models.IntegerField()
    managetag = models.IntegerField()
    managetagtpl = models.IntegerField()
    managealbum = models.IntegerField()
    managecomment = models.IntegerField()
    managemtag = models.IntegerField()
    managethread = models.IntegerField()
    manageevent = models.IntegerField()
    manageeventclass = models.IntegerField()
    managecensor = models.IntegerField()
    managead = models.IntegerField()
    managesitefeed = models.IntegerField()
    managebackup = models.IntegerField()
    manageblock = models.IntegerField()
    managetemplate = models.IntegerField()
    managestat = models.IntegerField()
    managecache = models.IntegerField()
    managecredit = models.IntegerField()
    managecron = models.IntegerField()
    managename = models.IntegerField()
    manageapp = models.IntegerField()
    managetask = models.IntegerField()
    managereport = models.IntegerField()
    managepoll = models.IntegerField()
    manageclick = models.IntegerField()
    managemagic = models.IntegerField()
    managemagiclog = models.IntegerField()
    managebatch = models.IntegerField()
    managedelspace = models.IntegerField()
    managetopic = models.IntegerField()
    manageip = models.IntegerField()
    managehotuser = models.IntegerField()
    managedefaultuser = models.IntegerField()
    managespacegroup = models.IntegerField()
    managespaceinfo = models.IntegerField()
    managespacecredit = models.IntegerField()
    managespacenote = models.IntegerField()
    managevideophoto = models.IntegerField()
    managelog = models.IntegerField()
    magicaward = models.TextField()
    sendsms = models.IntegerField()
    maxsmsnum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_usergroup'


class IhomeUserlog(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    action = models.CharField(max_length=10)
    type = models.IntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_userlog'


class IhomeUsermagic(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    mid = models.CharField(max_length=15)
    count = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_usermagic'
        unique_together = (('uid', 'mid'),)


class IhomeUsertask(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    taskid = models.PositiveSmallIntegerField()
    credit = models.SmallIntegerField()
    dateline = models.PositiveIntegerField()
    isignore = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_usertask'
        unique_together = (('uid', 'taskid'),)


class IhomeVideo(models.Model):
    albumid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    hot = models.IntegerField()
    postip = models.CharField(max_length=20)
    filename = models.CharField(max_length=100)
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=400)
    size = models.PositiveIntegerField()
    filepath = models.CharField(max_length=60)
    view = models.IntegerField()
    request = models.IntegerField()
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    noreply = models.IntegerField()
    comment = models.IntegerField()
    share = models.IntegerField()
    abstract = models.CharField(max_length=200)
    picid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_video'


class IhomeVisitor(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    vuid = models.PositiveIntegerField()
    vusername = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_visitor'
        unique_together = (('uid', 'vuid'),)


class IhomeWall(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    wallname = models.CharField(max_length=30)
    content = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField()
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    starttime = models.IntegerField()
    endtime = models.IntegerField()
    timeline = models.IntegerField()
    live = models.IntegerField(blank=True, null=True)
    check = models.IntegerField()
    wallurl = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihome_wall'


class IhomeWallfield(models.Model):
    uid = models.IntegerField()
    username = models.CharField(max_length=30, blank=True, null=True)
    message = models.CharField(max_length=140)
    pass_field = models.IntegerField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    display = models.IntegerField()
    now = models.IntegerField()
    timeline = models.IntegerField()
    hot = models.IntegerField()
    ip = models.CharField(max_length=64)
    wallid = models.SmallIntegerField(blank=True, null=True)
    floorid = models.IntegerField()
    feedid = models.IntegerField(blank=True, null=True)
    checktime = models.IntegerField(blank=True, null=True)
    fromdevice = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ihome_wallfield'


class IhomeWalluser(models.Model):
    wfid = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihome_walluser'
        unique_together = (('id', 'wfid', 'userid'),)


class IhomeuserAdmins(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=15)
    allowadminsetting = models.IntegerField()
    allowadminapp = models.IntegerField()
    allowadminuser = models.IntegerField()
    allowadminbadword = models.IntegerField()
    allowadmintag = models.IntegerField()
    allowadminpm = models.IntegerField()
    allowadmincredits = models.IntegerField()
    allowadmindomain = models.IntegerField()
    allowadmindb = models.IntegerField()
    allowadminnote = models.IntegerField()
    allowadmincache = models.IntegerField()
    allowadminlog = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_admins'


class IhomeuserApplications(models.Model):
    appid = models.PositiveSmallIntegerField(primary_key=True)
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    authkey = models.CharField(max_length=255)
    ip = models.CharField(max_length=15)
    viewprourl = models.CharField(max_length=255)
    apifilename = models.CharField(max_length=30)
    charset = models.CharField(max_length=8)
    dbcharset = models.CharField(max_length=8)
    synlogin = models.IntegerField()
    recvnote = models.IntegerField(blank=True, null=True)
    extra = models.TextField()
    tagtemplates = models.TextField()
    allowips = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_applications'


class IhomeuserBadwords(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    admin = models.CharField(max_length=15)
    find = models.CharField(unique=True, max_length=255)
    replacement = models.CharField(max_length=255)
    findpattern = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ihomeuser_badwords'


class IhomeuserDomains(models.Model):
    domain = models.CharField(max_length=40)
    ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ihomeuser_domains'


class IhomeuserFailedlogins(models.Model):
    ip = models.CharField(primary_key=True, max_length=15)
    count = models.PositiveIntegerField()
    lastupdate = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_failedlogins'


class IhomeuserFeeds(models.Model):
    feedid = models.AutoField(primary_key=True)
    appid = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    dateline = models.PositiveIntegerField()
    hash_template = models.CharField(max_length=32)
    hash_data = models.CharField(max_length=32)
    title_template = models.TextField()
    title_data = models.TextField()
    body_template = models.TextField()
    body_data = models.TextField()
    body_general = models.TextField()
    image_1 = models.CharField(max_length=255)
    image_1_link = models.CharField(max_length=255)
    image_2 = models.CharField(max_length=255)
    image_2_link = models.CharField(max_length=255)
    image_3 = models.CharField(max_length=255)
    image_3_link = models.CharField(max_length=255)
    image_4 = models.CharField(max_length=255)
    image_4_link = models.CharField(max_length=255)
    target_ids = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ihomeuser_feeds'


class IhomeuserFriends(models.Model):
    uid = models.PositiveIntegerField()
    friendid = models.PositiveIntegerField()
    direction = models.IntegerField()
    version = models.AutoField(primary_key=True)
    delstatus = models.IntegerField()
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ihomeuser_friends'


class IhomeuserMailqueue(models.Model):
    mailid = models.AutoField(primary_key=True)
    touid = models.PositiveIntegerField()
    tomail = models.CharField(max_length=32)
    frommail = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    charset = models.CharField(max_length=15)
    htmlon = models.IntegerField()
    level = models.IntegerField()
    dateline = models.PositiveIntegerField()
    failures = models.PositiveIntegerField()
    appid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_mailqueue'


class IhomeuserMemberfields(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    blacklist = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_memberfields'


class IhomeuserMembers(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    myid = models.CharField(max_length=30)
    myidkey = models.CharField(max_length=16)
    regip = models.CharField(max_length=15)
    regdate = models.PositiveIntegerField()
    lastloginip = models.IntegerField()
    lastlogintime = models.PositiveIntegerField()
    salt = models.CharField(max_length=6)
    secques = models.CharField(max_length=8)
    password1 = models.CharField(max_length=32, blank=True, null=True)
    m_online = models.IntegerField()
    weibo_uid = models.BigIntegerField(unique=True, blank=True, null=True)
    weibo_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ihomeuser_members'


class IhomeuserMergemembers(models.Model):
    appid = models.PositiveSmallIntegerField(primary_key=True)
    username = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ihomeuser_mergemembers'
        unique_together = (('appid', 'username'),)


class IhomeuserNewpm(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ihomeuser_newpm'


class IhomeuserNotelist(models.Model):
    noteid = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=32)
    closed = models.IntegerField()
    totalnum = models.PositiveSmallIntegerField()
    succeednum = models.PositiveSmallIntegerField()
    getdata = models.TextField()
    postdata = models.TextField()
    dateline = models.PositiveIntegerField()
    pri = models.IntegerField()
    app1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_notelist'


class IhomeuserPmIndexes(models.Model):
    pmid = models.AutoField(primary_key=True)
    plid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_indexes'


class IhomeuserPmLists(models.Model):
    plid = models.AutoField(primary_key=True)
    authorid = models.PositiveIntegerField()
    pmtype = models.PositiveIntegerField()
    subject = models.CharField(max_length=80)
    members = models.PositiveSmallIntegerField()
    min_max = models.CharField(max_length=17)
    dateline = models.PositiveIntegerField()
    lastmessage = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_lists'


class IhomeuserPmMembers(models.Model):
    plid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    isnew = models.PositiveIntegerField()
    pmnum = models.PositiveIntegerField()
    lastupdate = models.PositiveIntegerField()
    lastdateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_members'
        unique_together = (('plid', 'uid'),)


class IhomeuserPmMessages0(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_0'


class IhomeuserPmMessages1(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_1'


class IhomeuserPmMessages2(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_2'


class IhomeuserPmMessages3(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_3'


class IhomeuserPmMessages4(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_4'


class IhomeuserPmMessages5(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_5'


class IhomeuserPmMessages6(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_6'


class IhomeuserPmMessages7(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_7'


class IhomeuserPmMessages8(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_8'


class IhomeuserPmMessages9(models.Model):
    pmid = models.PositiveIntegerField(primary_key=True)
    plid = models.PositiveIntegerField()
    authorid = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pm_messages_9'


class IhomeuserPms(models.Model):
    pmid = models.AutoField(primary_key=True)
    msgfrom = models.CharField(max_length=15)
    msgfromid = models.PositiveIntegerField()
    msgtoid = models.PositiveIntegerField()
    folder = models.CharField(max_length=6)
    new = models.IntegerField()
    subject = models.CharField(max_length=75)
    dateline = models.PositiveIntegerField()
    message = models.TextField()
    delstatus = models.PositiveIntegerField()
    related = models.PositiveIntegerField()
    fromappid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_pms'


class IhomeuserProtectedmembers(models.Model):
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=15)
    appid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    admin = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ihomeuser_protectedmembers'
        unique_together = (('username', 'appid'),)


class IhomeuserSettings(models.Model):
    k = models.CharField(primary_key=True, max_length=32)
    v = models.TextField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_settings'


class IhomeuserSqlcache(models.Model):
    sqlid = models.CharField(primary_key=True, max_length=6)
    data = models.CharField(max_length=100)
    expiry = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_sqlcache'


class IhomeuserTags(models.Model):
    tagname = models.CharField(max_length=20)
    appid = models.PositiveSmallIntegerField()
    data = models.TextField(blank=True, null=True)
    expiration = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ihomeuser_tags'


class IhomeuserVars(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ihomeuser_vars'


class Lastsucc(models.Model):
    lastend = models.CharField(primary_key=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'lastsucc'


class MoodlensRealtime(models.Model):
    end = models.IntegerField(primary_key=True)
    duration = models.IntegerField()
    sentiment = models.IntegerField()
    count = models.IntegerField()
    keywords = models.TextField()
    weibos = models.TextField()

    class Meta:
        managed = False
        db_table = 'moodlens_realtime'
        unique_together = (('end', 'duration', 'sentiment'),)


class Temp(models.Model):
    id = models.IntegerField()
    uid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    replynum = models.BigIntegerField()
    replysecs = models.DecimalField(max_digits=33, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class TmpMa(models.Model):
    id = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    dateline = models.DateTimeField(blank=True, null=True)
    replynum = models.IntegerField(blank=True, null=True)
    replysecs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_ma'
