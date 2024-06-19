-- Lesson 39: ���������� � SQL
-- 24.04.2024

-- SELECT - ������� (�������)
-- FROM - �� (�������)
-- ; - ����� �������
-- ������������������� ����

SELECT *
FROM MarvelCharacters;

SELECT name, identify, hair, sex, appearances
FROM MarvelCharacters;

-- �� ����� ������������ ������� ����������
-- WHERE - ���, ����� ����� SELECT � ����� FROM

-- ���������, ��� ��������� ������ 100
SELECT name, identify, hair, appearances
FROM MarvelCharacters
WHERE appearances > 100;

-- ORDER BY - ����������� �� (�������) DESC - �� ��������
-- ���������� ����� ���� �� ���������� ��������
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100
ORDER BY HAIR, name;


-- � WHERE ����� ���� ���������� ������� (������� �� ������)
-- ��������� ���������� ����������
-- () - ������. ������� ����������� ������ ������
-- NOT - ��
-- AND - �
-- OR - ���
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100 and sex = "Female Characters"
ORDER BY APPEARANCES DESC;

-- DISTINCT - ���������� ��������

SELECT DISTINCT sex
FROM MarvelCharacters
WHERE sex not null;


-- LIMIT - ���������� ���������� �����
-- OFFSET - ���������� ������
SELECT name, APPEARANCES, year
FROM MarvelCharacters
WHERE year = 1962
ORDER BY APPEARANCES DESC
LIMIT 5
OFFSET 3

-- ������ ���������� - ��� ��������� �� ���� �������� �����)

-- �������� ���������� � ������ ������ ����
-- No Eyes, Compound Eyes, Multiple Eyes, Variable Eyes, One Eye,


SELECT name, APPEARANCES, year, eye
FROM MarvelCharacters
WHERE eye = "No Eyes" OR eye = "Compound Eyes" OR eye = "Multiple Eyes" OR eye = "Variable Eyes" OR eye = "One Eye"
ORDER BY APPEARANCES DESC

-- IN - ������ � ������
-- NOT IN - �� ������ � ������

SELECT name, APPEARANCES, year, eye
FROM MarvelCharacters
WHERE eye IN ("No Eyes", "Compound Eyes", "Multiple Eyes", "Variable Eyes", "One Eye")
ORDER BY APPEARANCES DESC


-- ������ ���������� ������ �� ������� ����������:
-- SELECT - ������� (�������)
-- FROM - �� (�������)
-- ; - ����� �������
-- WHERE - ���
-- ORDER BY - ����������� �� (�������)
-- DESC - �� ��������
-- () - ������
-- NOT - ��
-- AND - �
-- OR - ���

-- DISTINCT - ���������� ��������
-- LIMIT - ���������� ���������� �����
-- OFFSET - ���������� ������
-- IN - ������ � ������
-- NOT IN - �� ������ � ������
