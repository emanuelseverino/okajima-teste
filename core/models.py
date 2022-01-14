from django.db import models


class AppLogin(models.Model):
    codigorca = models.DecimalField(db_column='CODIGORCA', max_digits=4, decimal_places=0, primary_key=True)  # Field name made lowercase.
    nomerca = models.CharField(db_column='NOMERCA', max_length=40)  # Field name made lowercase.
    codigosv = models.DecimalField(db_column='CODIGOSV', max_digits=4, decimal_places=0)  # Field name made lowercase.
    nomesv = models.CharField(db_column='NOMESV', max_length=40)  # Field name made lowercase.
    codigocv = models.DecimalField(db_column='CODIGOCV', max_digits=4, decimal_places=0, blank=True,
                                   null=True)  # Field name made lowercase.
    nomecv = models.CharField(db_column='NOMECV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='MODELO', max_length=16, blank=True, null=True)  # Field name made lowercase.
    faixa = models.CharField(db_column='FAIXA', max_length=14, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    funcao = models.CharField(db_column='FUNCAO', max_length=13, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APP_LOGIN'

    def __str__(self):
        return self.nomecv


class AppSamuraicupom(models.Model):
    codigorca = models.IntegerField(db_column='CODIGORCA', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=196, db_collation='utf8_general_ci', blank=True,
                                 null=True)  # Field name made lowercase.
    metavenda = models.IntegerField(db_column='METAVENDA', blank=True, null=True)  # Field name made lowercase.
    venda = models.DecimalField(db_column='VENDA', max_digits=65, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    percvenda = models.DecimalField(db_column='PERCVENDA', max_digits=65, decimal_places=2, blank=True,
                                    null=True)  # Field name made lowercase.
    metapos = models.IntegerField(db_column='METAPOS', blank=True, null=True)  # Field name made lowercase.
    pos = models.IntegerField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    percpos = models.DecimalField(db_column='PERCPOS', max_digits=65, decimal_places=2, blank=True,
                                  null=True)  # Field name made lowercase.
    qt_cupons = models.IntegerField(db_column='QT_CUPONS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APP_SAMURAICUPOM'


class ShowMeta(models.Model):
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    codcv = models.IntegerField(db_column='CODCV', blank=True, null=True)  # Field name made lowercase.
    codsv = models.IntegerField(db_column='CODSV', blank=True, null=True)  # Field name made lowercase.
    codigorca = models.IntegerField(db_column='CODIGORCA', primary_key=True)  # Field name made lowercase.
    codfornec = models.IntegerField(db_column='CODFORNEC', blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.CharField(db_column='FORNECEDOR', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=30, blank=True,
                                 null=True)  # Field name made lowercase.
    metavalor = models.IntegerField(db_column='METAVALOR', blank=True, null=True)  # Field name made lowercase.
    metapositivacao = models.IntegerField(db_column='METAPOSITIVACAO', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHOW_META'

    def __str__(self):
        return str(self.codigorca) + ' - ' + str(self.categoria) + ' - ' + str(self.metavalor)


# ______________________________________________________

class AppCupons(models.Model):
    codigorca = models.DecimalField(db_column='CODIGORCA', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    codigosv = models.DecimalField(db_column='CODIGOSV', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=80, blank=True, null=True)  # Field name made lowercase.
    metavenda = models.DecimalField(db_column='METAVENDA', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    venda = models.DecimalField(db_column='VENDA', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    meta_pos = models.DecimalField(db_column='META_POS', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pos = models.BigIntegerField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    qt_cupons = models.IntegerField(db_column='QT_CUPONS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APP_CUPONS'



class AppMatinal(models.Model):
    codsuperv = models.IntegerField(db_column='CODSUPERV', blank=True, null=True)  # Field name made lowercase.
    codrca = models.IntegerField(db_column='CODRCA', blank=True, null=True)  # Field name made lowercase.
    rca = models.CharField(db_column='RCA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    clicad = models.IntegerField(db_column='CLICAD', blank=True, null=True)  # Field name made lowercase.
    cliativos = models.IntegerField(db_column='CLIATIVOS', blank=True, null=True)  # Field name made lowercase.
    metavenda = models.FloatField(db_column='METAVENDA', blank=True, null=True)  # Field name made lowercase.
    venda = models.FloatField(db_column='VENDA', blank=True, null=True)  # Field name made lowercase.
    metapos = models.IntegerField(db_column='METAPOS', blank=True, null=True)  # Field name made lowercase.
    positivacao = models.IntegerField(db_column='POSITIVACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APP_MATINAL'


class AppMetageral(models.Model):
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codigorca = models.IntegerField(db_column='CODIGORCA', blank=True, null=True)  # Field name made lowercase.
    meta = models.DecimalField(db_column='META', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APP_METAGERAL'



class ShowRca(models.Model):
    codigorca = models.IntegerField(db_column='CODIGORCA')  # Field name made lowercase.
    nomerca = models.CharField(db_column='NOMERCA', max_length=60)  # Field name made lowercase.
    codsv = models.IntegerField(db_column='CODSV')  # Field name made lowercase.
    nomesv = models.CharField(db_column='NOMESV', max_length=60)  # Field name made lowercase.
    codcv = models.IntegerField(db_column='CODCV')  # Field name made lowercase.
    nomecv = models.CharField(db_column='NOMECV', max_length=60)  # Field name made lowercase.
    modelo = models.CharField(db_column='MODELO', max_length=60)  # Field name made lowercase.
    faixa = models.CharField(db_column='FAIXA', max_length=60)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHOW_RCA'


class ShowRevista(models.Model):
    codcli = models.IntegerField(db_column='CODCLI', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fantasia = models.CharField(db_column='FANTASIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codrca = models.IntegerField(db_column='CODRCA', blank=True, null=True)  # Field name made lowercase.
    foto = models.CharField(db_column='FOTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recebido = models.CharField(db_column='RECEBIDO', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHOW_REVISTA'


class ShowVenda(models.Model):
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    codcv = models.IntegerField(db_column='CODCV', blank=True, null=True)  # Field name made lowercase.
    codsv = models.IntegerField(db_column='CODSV')  # Field name made lowercase.
    codigorca = models.IntegerField(db_column='CODIGORCA', blank=True, null=True)  # Field name made lowercase.
    codigofornecedor = models.IntegerField(db_column='CODIGOFORNECEDOR', blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.CharField(db_column='FORNECEDOR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=80, blank=True, null=True)  # Field name made lowercase.
    codigocliente = models.IntegerField(db_column='CODIGOCLIENTE')  # Field name made lowercase.
    valor = models.DecimalField(db_column='VALOR', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHOW_VENDA'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id = models.BigAutoField(primary_key=True)
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
