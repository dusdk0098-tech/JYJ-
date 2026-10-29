def test_unknown_format_and_text_view_keep_korean(viewer, page):
    viewer("unsupported.html", "unknown.xyz", lang="ko")
    assert page.locator(".card h2").inner_text() == "제이웹리더기에서 이 형식을 인식할 수 없습니다"
    assert page.locator("#asText").inner_text() == "텍스트로 보기"
    page.locator("#asText").click()
    page.wait_for_url("**/text.html*")
    assert "lang=ko" in page.url
    assert page.title() == "텍스트"


def test_korean_book_controls_leave_document_content_unchanged(viewer, page):
    viewer("epub.html", "almanac.epub", lang="ko")
    page.get_by_text("The almanac opens at dawn.").wait_for()
    assert page.locator("#epub-contents-open").inner_text() == "목차"
    assert page.locator("#epub-next").inner_text() == "다음"
    assert page.get_by_text("The almanac opens at dawn.").is_visible()


def test_korean_pdf_password_prompt(viewer, page):
    viewer("pdf.html", "encrypted.pdf", lang="ko")
    page.locator("#vw-pw").wait_for()
    assert "비밀번호로 보호된 PDF" in page.locator("#vw-status").inner_text()
    assert page.locator(".vw-ask-btn").inner_text() == "열기"


def test_english_remains_available(viewer, page):
    viewer("unsupported.html", "unknown.xyz", lang="en")
    assert page.locator("#asText").inner_text() == "View as text"
