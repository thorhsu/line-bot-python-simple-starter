from linebot.models import (
    TemplateSendMessage, 
    CarouselTemplate, 
    CarouselColumn,
    MessageAction,
    URIAction
)
class Menu:
    def __init__(self):
        self.content = TemplateSendMessage(
            # 如果顯示不出模版時的替代文字
            alt_text='Carousel template',
            # Carousel是卡片，有上限，三或四張，超過無法顯示
            template=CarouselTemplate(
                columns=[
                    # CarouselColumn(),
                    # CarouselColumn(),
                    CarouselColumn(
                        thumbnail_image_url='https://picsum.photos/1200/600?image=684',
                        title='匯率選單',
                        text='點選你要查詢的貨幣',
                        actions=[
                            # action也有上限，最多三個
                            MessageAction(
                                label='查詢美金',
                                text='美金'
                            ),
                            MessageAction(
                                label='查詢日圓',
                                text='日圓'
                            ),
                            MessageAction(
                                label='查詢歐元',
                                text='歐元'
                            ),
                            # URIAction(
                            #     label='Google',
                            #     uri='https://google.com'
                            # )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://picsum.photos/1200/600?image=701',
                        title='匯率選單',
                        text='點選你要查詢的貨幣',
                        actions=[
                            MessageAction(
                                label='查詢港幣',
                                text='港幣'
                            ),
                            MessageAction(
                                label='查詢英鎊',
                                text='英鎊'
                            ),
                            MessageAction(
                                label='查詢人民幣',
                                text='人民幣'
                            )
                        ]
                    )
                ]
            )
        )