from django import forms

class ChatForm(forms.Form):
    # label: 사용자에게 보여지는 레이블
    # max_length: 사용자가 입력할 수 있는 최대 길이
    # widget: 사용자 입력창의 디자인을 변경할 수 있는 옵션
    # from-control: 입력창의 크기를 조절하는 클래스
    # placeholder: 입력창에 미리 보여지는 텍스트
    text_input = forms.CharField(
        label = "글 내용에 대해서 요약",
        max_length = 100,
        widget = forms.Textarea(attrs={
            'class' : 'form-control',
            'placeholder' : '요약할 글 내용을 입력하세요',
            'rows' : 4, # 입력창의 높이를 조절
        }),
        required = False # 필수 입력 항목이 아님
    )
    file_input = forms.FileField(
        label = "PDF 파일 업로드",
        widget = forms.ClearableFileInput(attrs={
            'class' : 'form-control'
        }),
        required = False # 비워도 괜찮은 필드
    )
    youtube_url = forms.URLField(
        label = "Youtube URL 요약",
        widget = forms.URLInput(attrs={
            'class' : 'form-control',
            'placeholder' : '요약할 Youtube URL을 입력하세요'
        }),
        required=False
    )