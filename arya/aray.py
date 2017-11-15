from arya.service import v1
from arya import models
from django.urls import reverse
from django.utils import six
from django.utils.safestring import mark_safe
from django.http.request import QueryDict
from django.shortcuts import HttpResponse,render
# ################# 用户表操作 #################
class UserAdmin(v1.BaseAryaModal):
    def edit_field(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:

            edit_url = reverse('{0}:{1}_{2}_change'.format(self.site.namespace, self.app_label, self.model_name),
                               args=(obj.pk,))
            del_url = reverse('{0}:{1}_{2}_delete'.format(self.site.namespace, self.app_label, self.model_name),
                              args=(obj.pk,))
            detail_url = reverse('{0}:{1}_{2}_detail'.format(self.site.namespace, self.app_label, self.model_name),
                                 args=(obj.pk,))

            param_url = ""
            if len(self.request.GET):
                _change = QueryDict(mutable=True)
                _change['_change_filter'] = self.request.GET.urlencode()
                param_url = "?{0}".format(_change.urlencode())

            tpl = "<a href='{0}{3}'>编辑</a> | <a href='{1}{3}'>删除</a> | <a href='{2}{3}'>查看详细</a>".format(edit_url,
                                                                                                         del_url,
                                                                                                         detail_url,
                                                                                                         param_url)
            return mark_safe(tpl)
    list_display = ['username','email',edit_field]

    actions = []

v1.site.register(models.User,UserAdmin)

# ################# 角色操作 #################
class RoleAdmin(v1.BaseAryaModal):
    actions = []

    def edit_field(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:

            edit_url = reverse('{0}:{1}_{2}_change'.format(self.site.namespace, self.app_label, self.model_name),
                               args=(obj.pk,))
            del_url = reverse('{0}:{1}_{2}_delete'.format(self.site.namespace, self.app_label, self.model_name),
                              args=(obj.pk,))
            detail_url = reverse('{0}:{1}_{2}_detail'.format(self.site.namespace, self.app_label, self.model_name),
                                 args=(obj.pk,))

            param_url = ""
            if len(self.request.GET):
                _change = QueryDict(mutable=True)
                _change['_change_filter'] = self.request.GET.urlencode()
                param_url = "?{0}".format(_change.urlencode())

            tpl = "<a href='{0}{3}'>编辑</a> | <a href='{1}{3}'>删除</a> | <a href='{2}{3}'>查看详细</a>".format(edit_url,
                                                                                                         del_url,
                                                                                                         detail_url,
                                                                                                         param_url)
            return mark_safe(tpl)
    list_display = ['caption',edit_field]

v1.site.register(models.Role,RoleAdmin)

# ################# 菜单操作 #################
class MenuAdmin(v1.BaseAryaModal):
    pass
v1.site.register(models.Menu,MenuAdmin)

# ################# 权限操作 #################
class PermissionAdmin(v1.BaseAryaModal):

    def edit_field(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:

            edit_url = reverse('{0}:{1}_{2}_change'.format(self.site.namespace, self.app_label, self.model_name),
                               args=(obj.pk,))
            del_url = reverse('{0}:{1}_{2}_delete'.format(self.site.namespace, self.app_label, self.model_name),
                              args=(obj.pk,))
            detail_url = reverse('{0}:{1}_{2}_detail'.format(self.site.namespace, self.app_label, self.model_name),
                                 args=(obj.pk,))

            param_url = ""
            if len(self.request.GET):
                _change = QueryDict(mutable=True)
                _change['_change_filter'] = self.request.GET.urlencode()
                param_url = "?{0}".format(_change.urlencode())

            tpl = "<a href='{0}{3}'>编辑</a> | <a href='{1}{3}'>删除</a> | <a href='{2}{3}'>查看详细</a>".format(edit_url,
                                                                                                         del_url,
                                                                                                         detail_url,
                                                                                                         param_url)
            return mark_safe(tpl)
    list_display = ['caption','url','menu',edit_field]

    actions = []

    def another_urls(self):
        from django.conf.urls import url
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urls = [
            url(r'^show/$', self.show, name='%s_%s_show' % info),
        ]
        return urls

    def show(self,request):
        print(request.method)
        current_user_id = request.session['user_info']['nid']

        return render(request,'permission_show.html')

v1.site.register(models.Permission,PermissionAdmin)

