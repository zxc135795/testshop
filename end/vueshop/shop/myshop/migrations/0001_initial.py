# Generated by Django 3.0.3 on 2020-03-09 06:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='catimg', verbose_name='分类图片')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodimg', models.ImageField(upload_to='goodimg', verbose_name='商品图')),
                ('name', models.CharField(max_length=20, verbose_name='商品名')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('quan', models.FloatField(default=10, verbose_name='优惠券')),
                ('coupon_price', models.FloatField(default=0, verbose_name='实际价格')),
                ('docs', models.CharField(max_length=20, verbose_name='商品描述')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='myshop.Category', verbose_name='所属分类')),
            ],
        ),
        migrations.CreateModel(
            name='ToImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='toimg', verbose_name='轮播图')),
            ],
        ),
        migrations.CreateModel(
            name='Youther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='youimg', verbose_name='卖家头像')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='ShoeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showimg', models.ImageField(upload_to='showimg', verbose_name='卖家展示图')),
                ('showdocs', models.CharField(max_length=500, verbose_name='卖家推荐言论')),
                ('docs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='youer', to='myshop.Youther', verbose_name='言论推荐人')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.ManyToManyField(to='myshop.Good', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
    ]
