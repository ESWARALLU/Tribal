from .models import TribeUser, TribalMember

def tribe_member_context(request):
    tribeMember = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = TribeUser.objects.get(id=user_id)
            tribeMember = TribalMember.objects.get(phno=user.phno)
        except (TribeUser.DoesNotExist, TribalMember.DoesNotExist):
            pass
    return {'tribeMember': tribeMember}
