# 제이웹리더기

제이웹리더기는 문서, 사진, 전자책 등 여러 형식의 파일을 한곳에서 열어 보는 안드로이드 앱입니다. 원본 오픈소스 앱 [Gander](https://github.com/mokshablr/gander)를 바탕으로 한국어 화면과 새로운 디자인을 적용했습니다.

[최신 버전 다운로드](https://github.com/dusdk0098-tech/JYJ-/releases/latest) · [소스코드](https://github.com/dusdk0098-tech/JYJ-) · [페딧 웹사이트](https://pedit.kr)

## 주요 기능

- PDF와 Word 문서, 스프레드시트, 슬라이드, 이미지, 동영상, 오디오, 전자책 등을 열 수 있습니다.
- 최근 파일과 사용자가 선택한 폴더를 살펴보고 파일 이름, 날짜 또는 크기로 정렬할 수 있습니다.
- 다른 앱에서 파일을 공유하거나 ‘다른 앱으로 열기’를 이용할 수 있습니다.
- 지원하는 문서에서 검색, 확대, 텍스트 복사, 인쇄와 이어 읽기를 사용할 수 있습니다. 형식에 따라 제공되는 기능은 다릅니다.
- ZIP 파일의 목록을 살펴보고 내부 파일을 열 수 있으며, STL 3D 모델을 회전하고 확대할 수 있습니다.
- 한국어 환경에서 앱의 안내와 메뉴를 한국어로 표시합니다. 흰색 배경과 하늘색을 활용한 화면을 제공합니다.

## 지원하는 파일

| 종류 | 주요 형식 |
| --- | --- |
| 문서 | PDF, Word, OpenDocument, RTF |
| 스프레드시트 | Excel, CSV, ODS |
| 슬라이드 | PPTX, PPSX, PPTM, POTX |
| 이미지 | JPG, PNG, GIF, WebP, HEIC, SVG 등 |
| 동영상과 오디오 | MP4, MKV, MP3, M4A, WAV 등 |
| 전자책 | DRM이 없는 EPUB |
| 그 밖의 파일 | Markdown, 텍스트, 코드, ZIP, STL |

전체 확장자 목록은 [지원 파일 형식 안내](app/src/main/assets/file_types_ko.md)에서 볼 수 있습니다. 오래된 PowerPoint `.ppt` 형식은 지원하지 않습니다. 파일에 포함된 일부 차트나 이미지 등은 표시가 제한될 수 있습니다.

## 설치

Android 8.0 이상에서 사용할 수 있습니다. [릴리스 페이지](https://github.com/dusdk0098-tech/JYJ-/releases/latest)에서 `JWebReader-2.7.apk`를 내려받아 설치하세요. 일부 문서 형식은 최신 Android 시스템 WebView가 필요할 수 있습니다.

GitHub에서 직접 설치할 때 Google Play 프로텍트가 앱 검사를 요청하거나 삼성 기기에서 보안 경고가 표시될 수 있습니다. 삼성에 이 APK의 보안 검토를 요청했으며, 결과는 아직 확인되지 않았습니다. 경고가 표시되면 안내에 따라 검사 결과를 확인하세요.

제이웹리더기는 원본 Gander와 다른 앱으로 설치되며, 기존 Gander 앱을 업데이트하거나 최근 파일과 폴더 접근 권한을 자동으로 가져오지 않습니다.

## 개인정보와 파일 접근

앱은 Android의 파일 선택기와 ‘다른 앱으로 열기’를 통해 사용자가 선택한 파일에 접근합니다. 문서 처리는 기기에서 이루어지며, 배포 APK는 인터넷 권한을 요청하지 않습니다. 앱 안의 페딧 웹사이트 링크는 선택하면 외부 브라우저에서 열립니다.

## 소스에서 빌드

JDK 21 이상과 Android SDK 플랫폼 36이 필요합니다.

```sh
./gradlew assembleDebug
./gradlew assembleRelease
```

배포 빌드는 저장소에 별도로 구성된 서명 키가 없다면 서명되지 않습니다. 본인의 키로 서명한 APK는 이 저장소의 릴리스 APK를 덮어 설치할 수 없습니다. 개인 서명 키와 비밀번호는 공개 저장소에 올리지 마세요.

## 제작 및 후원

- 제작: 조영진
- 도움: Arjun Maniyani
- 소스코드: [dusdk0098-tech/JYJ-](https://github.com/dusdk0098-tech/JYJ-)

커피 한 잔의 후원으로 불우이웃을 도와주세요.

농협 조영진 **352-0306-8434-63**

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다. 원본 Gander의 저작권은 Arjun Maniyani에게 있습니다. 포함된 외부 라이브러리의 라이선스 전문은 앱 정보 화면과 [라이선스 안내](app/src/main/assets/licences.md)에서 확인할 수 있습니다.
