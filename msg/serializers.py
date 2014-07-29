from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

from msg.models import Msg

class MsgSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Msg
        fields = ( 'subject','origin','channel','message_id','pubkey_list','miners_fee_satoshi','prevtxs','outputs','req_sigs','operation','sum_satoshi','locktime' )


