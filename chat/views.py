from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import ChatForm
from openai import OpenAI
from django.conf import settings
from django.views.generic import TemplateView
import fitz  # PyMuPDF 라이브러리

# 클라이언트 인스턴스 생성
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_completion(prompt, model="gpt-3.5-turbo"):
    try:
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.5
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"
    
def generate_prompt(text_input=None, file_input=None):
    if text_input:
        return f"다음 내용을 10줄 이내로 요약해줘: {text_input}"
    elif file_input:
        file_content = extract_text_from_pdf(file_input)
        return f"다음 PDF 파일 내용을 10줄 이내로 요약해줘: {file_content}"
    else:
        return "요약할 내용이 없습니다."
    
def extract_text_from_pdf(pdf_file):
    # PDF 파일에서 텍스트를 추출하는 함수.
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

class ChatView(LoginRequiredMixin, FormView):
    template_name = 'chat/index.html'
    form_class = ChatForm
    success_url = '/'  # 폼 제출 후 다시 메인 페이지로 리디렉션

    def form_valid(self, form):
        text_input = form.cleaned_data.get('text_input')
        file_input = form.cleaned_data.get('file_input')

        prompt = generate_prompt(text_input, file_input)
        result = get_completion(prompt)
        return self.render_to_response(self.get_context_data(result=result))

class HomeView(TemplateView):
    template_name = 'chat/home.html'