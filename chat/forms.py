from django import forms


class ChatForm(forms.Form):
    # label: 사용자에게 보여지는 레이블
    # max_length: 사용자가 입력할 수 있는 최대 길이
    # widget: 사용자 입력창의 디자인을 변경할 수 있는 옵션
    # from-control: 입력창의 크기를 조절하는 클래스
    # placeholder: 입력창에 미리 보여지는 텍스트
    text_input = forms.CharField(
        label='글 내용 요약',
        max_length=1000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': '요약할 내용을 입력하세요...',
            'rows': 4,
        }),
        required=False
    )
    file_input = forms.FileField(
        label='PDF 파일 요약',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )