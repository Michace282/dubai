from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from backend.mixin import TimeStampedModel
from colorfield.fields import ColorField
from account.models import Guest, Code
from django.contrib.auth.models import User
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend


class SizeChart(TimeStampedModel):
    name = models.CharField(verbose_name='Name size chart', max_length=30)
    table = models.TextField(verbose_name='Table')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size Chart'
        verbose_name_plural = 'Size Charts'


class Size(TimeStampedModel):
    chart = models.ForeignKey(SizeChart, verbose_name='Chart', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name size', max_length=30)

    def __str__(self):
        return f'{self.name}, ({str(self.chart)})'

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Color(TimeStampedModel):
    name = models.CharField(verbose_name='Name color', max_length=30)
    description = models.CharField(verbose_name='Description', max_length=30, blank=True, null=True)
    color = ColorField(verbose_name='Color', default='#FFFFFF')
    image = models.ImageField(verbose_name='Image(64x64)',
                              help_text='If an image is uploaded, it will be displayed in colors.',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Product(TimeStampedModel):
    class StatusType(DjangoChoices):
        published = ChoiceItem(label='Published', value='published')
        unpublished = ChoiceItem(label='Unpublished', value='unpublished')
        moderated = ChoiceItem(label='Moderated', value='moderated')

    class ProductType(DjangoChoices):
        ladies = ChoiceItem(label='Ladies', value='ladies')
        mens = ChoiceItem(label='Mens', value='mens')
        accessories = ChoiceItem(label='Accessories', value='accessories')
        dance_shoes = ChoiceItem(label='Dance shoes', value='dance_shoes')

    class LadiesType(DjangoChoices):
        body = ChoiceItem(label='Body', value='body')
        blouses = ChoiceItem(label='Blouses', value='blouses')
        skirts = ChoiceItem(label='Skirts', value='skirts')
        dresses = ChoiceItem(label='Dresses', value='dresses')
        trousers = ChoiceItem(label='Trousers', value='trousers')
        jumpsuits = ChoiceItem(label='Jumpsuits', value='jumpsuits')
        tops = ChoiceItem(label='Tops', value='tops')
        shorts = ChoiceItem(label='Shorts', value='shorts')

    class MensType(DjangoChoices):
        trousers = ChoiceItem(label='Trousers', value='trousers')
        waistcoasts = ChoiceItem(label='Waistcoasts', value='waistcoasts')
        shirts = ChoiceItem(label='Shirts', value='shirts')
        t_shirts = ChoiceItem(label='T-shirts', value='t_shirts')

    class AccessoriesType(DjangoChoices):
        shoe_accessories = ChoiceItem(label='Shoe accessories', value='shoe_accessories')
        bags = ChoiceItem(label='Bags', value='bags')
        ladies_accessories = ChoiceItem(label='Ladies accessories', value='ladies_accessories')
        t_shirts = ChoiceItem(label='T-shirts', value='t_shirts')

    class DanceShoesType(DjangoChoices):
        ladies = ChoiceItem(label='Ladies', value='ladies')
        mens = ChoiceItem(label='Mens', value='mens')

    status = models.CharField(verbose_name='Status',
                              max_length=30,
                              choices=StatusType.choices,
                              default=StatusType.published)

    name = models.CharField(verbose_name='Model name', max_length=30)
    product_type = models.CharField(verbose_name='Product type',
                                    max_length=30,
                                    choices=ProductType.choices)

    ladies_type = models.CharField(verbose_name='Ladies type',
                                   max_length=30,
                                   choices=LadiesType.choices,
                                   blank=True,
                                   null=True)

    mens_type = models.CharField(verbose_name='Mens type',
                                 max_length=30,
                                 choices=MensType.choices,
                                 blank=True,
                                 null=True)

    accessories_type = models.CharField(verbose_name='Accessories type',
                                        choices=AccessoriesType.choices,
                                        max_length=30,
                                        blank=True,
                                        null=True)

    dance_shoes_type = models.CharField(verbose_name='Dance shoes type',
                                        max_length=30,
                                        choices=DanceShoesType.choices, blank=True,
                                        null=True)

    article = models.CharField(verbose_name='Article', max_length=30)
    price = models.PositiveIntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    model_description = models.TextField(verbose_name='Model description', blank=True, null=True)
    size_chart = models.ForeignKey(SizeChart, verbose_name='Size Chart', on_delete=models.CASCADE, blank=True,
                                   null=True)

    data = models.TextField(blank=True, null=True)
    works_best_with = models.ManyToManyField('product.Product', verbose_name='Works best with', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductSizeColor(TimeStampedModel):
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name='Color', on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, verbose_name='Size')
    is_available = models.BooleanField(verbose_name='Is it available?', default=True)

    class Meta:
        unique_together = ('product', 'color')

    def __str__(self):
        return f'{str(self.color)}'

    class Meta:
        verbose_name = 'Product color'
        verbose_name_plural = 'Product colors'


class ProductImage(TimeStampedModel):
    product_size_color = models.ForeignKey(ProductSizeColor, verbose_name='Product Size Color',
                                           on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to='product/image')
    cropping = ImageRatioField('image', '350x500')

    def __str__(self):
        return str(self.product_size_color)

    @property
    def image_cropping(self):
        if self.image:
            return get_backend().get_thumbnail_url(self.image, {
                'box': self.cropping,
                'size': (350, 500),
                'crop': True,
                'detail': True,
            })
            return
        else:
            return ''

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'


class ProductWishlist(TimeStampedModel):
    guest = models.ForeignKey(Guest, verbose_name='Guest', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)


class Basket(TimeStampedModel):
    class StatusType(DjangoChoices):
        completed = ChoiceItem(label='Completed', value='completed')
        sent = ChoiceItem(label='Sent', value='sent')
        processing = ChoiceItem(label='Processing', value='processing')
        new = ChoiceItem(label='New', value='new')
        rejected = ChoiceItem(label='rejected', value='rejected')

    code = models.ForeignKey(Code, verbose_name='Code', on_delete=models.CASCADE, blank=True, null=True)
    discount = models.IntegerField(verbose_name='Discount', default=0)
    guest = models.ForeignKey(Guest, verbose_name='Guest', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(verbose_name='Status',
                              max_length=30,
                              choices=StatusType.choices,
                              default=StatusType.new)


class ProductBasket(TimeStampedModel):
    basket = models.ForeignKey(Basket, verbose_name='Basket', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Price')
    count = models.PositiveIntegerField(verbose_name='Count')
    size = models.ForeignKey(Size, verbose_name='Size', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name='Color', on_delete=models.CASCADE)


class Feedback(TimeStampedModel):
    class StatusType(DjangoChoices):
        published = ChoiceItem(label='Published', value='published')
        unpublished = ChoiceItem(label='Unpublished', value='unpublished')
        moderated = ChoiceItem(label='Moderated', value='moderated')

    class StarType(DjangoChoices):
        star1 = ChoiceItem(label='star1', value=1)
        star2 = ChoiceItem(label='star2', value=2)
        star3 = ChoiceItem(label='star3', value=3)
        star4 = ChoiceItem(label='star4', value=4)
        star5 = ChoiceItem(label='star5', value=5)

    guest = models.ForeignKey(Guest, verbose_name='Guest', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name='Size', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name='Color', on_delete=models.CASCADE)

    status = models.CharField(verbose_name='Status',
                              max_length=30,
                              choices=StatusType.choices,
                              default=StatusType.moderated)

    star = models.IntegerField(verbose_name='Star',
                               choices=StarType.choices)

    text = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        unique_together = ('product', 'color',)


class FeedbackImage(TimeStampedModel):
    feedback = models.ForeignKey(Feedback, verbose_name='Feedback',
                                 on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to='feedback/image')

    def __str__(self):
        return str(self.feedback)

    class Meta:
        verbose_name = 'Feedback image'
        verbose_name_plural = 'Feedback images'
