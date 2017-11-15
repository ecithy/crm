from arya.service import v1
from crm import models
from crm.views.branch import BranchAdmin


v1.site.register(models.Branch,BranchAdmin)