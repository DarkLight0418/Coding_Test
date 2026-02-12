# [level 0] 대소문자 바꿔서 출력하기 - 181949 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181949) 

### 성능 요약

메모리: 7.34 MB, 시간: 15.55 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 02월 12일 09:48:07

### 문제 설명

<p>영어 알파벳으로 이루어진 문자열 <code>str</code>이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>str</code>의 길이 ≤ 20

<ul>
<li><code>str</code>은 알파벳으로 이루어진 문자열입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>

<p>입력 #1</p>
<div class="highlight"><pre class="codehilite"><code>aBcDeFg
</code></pre></div>
<p>출력 #1</p>
<div class="highlight"><pre class="codehilite"><code>AbCdEfG
</code></pre></div>
<hr>

<p>※2023년 05월 03일 제한사항이 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

### 대소문자 바꿔서 출력 명세 정리

입력:
- 길이 1 이상 20 이하의 영어 알파벳 문자열 s

출력:
- 문자열 s의 각 문자의 대소문자를 반전시킨 문자열

제약 조건:
- 1 ≤ len(s) ≤ 20
- s는 오직 알파벳(A–Z, a–z)으로만 구성
---

문제 정의:
문자열의 각 문자를 순회하며 대소문자를 반전한다.

처리 규칙:
- 문자가 소문자이면 대문자로 변환
- 문자가 대문자이면 소문자로 변환

시간 복잡도:
- O(n) (문자열 길이 n에 대해 한 번 순회)

공간 복잡도:
- O(n) (새 문자열 생성)
