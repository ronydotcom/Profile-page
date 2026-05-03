from django import forms
from tasks.models import TaskModel,ProfileModel,ProductModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields=['title','description','status','due_date']
        exclude=['created_by']
        widgets={
            'due_date':forms.DateInput(attrs={'type' : 'date'}),
        }
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model= ProfileModel
        fields='__all__'
        exclude = ['user']
        widgets= {
            'date_of_birth' : forms.DateInput(attrs= {
                'type' : 'date'
            })
        }
        
        
        ##product
        
class ProductForm(forms.ModelForm):
    class Meta:
        model= ProductModel
        fields='__all__'
        exclude=['created_by','total_amount']