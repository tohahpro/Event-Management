from django import forms
from event.models import Events, Category


class StyleForMixin:
    """ Mixing to apply style to form field"""

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()

    default_classes = "border border-gray-300 w-full py-1 px-2 rounded shadow-sm focus:outline-none bg-[#FDF6EA] focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                }),
                
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("Inside Date")
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 rounded shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500 bg-[#FDF6EA]"
                })
            elif isinstance(field.widget, forms.TimeInput):
                print("Inside Date")
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 rounded shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500 bg-[#FDF6EA]"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                print("Inside checkbox")
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                print("Inside else")
                field.widget.attrs.update({
                    'class': self.default_classes
                })

class EventModelFrom(StyleForMixin,forms.ModelForm):
    class Meta:
        model= Events  
        fields = ['name','description','due_date','due_time','location']
        labels = {
            'name': 'Event Name',
            'description':'Event Details',
            'due_date': 'Enter Date',
            'due_time': 'Enter Time',
        }
        widgets = {
            'due_date' : forms.SelectDateWidget,
            'due_time' : forms.TimeInput(attrs={           
            'type': 'time'
            })            
        }      

class CategoryModelForm(StyleForMixin,forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'Event Category',
        }