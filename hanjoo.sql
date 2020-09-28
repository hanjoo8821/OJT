CREATE TABLE AB1_2
(
	NAME	  NVARCHAR2(8)	NOT NULL,
	EMP_NUM   NUMBER(7) NOT NULL,
	EMAIL 	  NVARCHAR2(40),
	PHONE	  NVARCHAR2(30),
	ROOM	  NUMBER(4),
	BIRTH	  DATE,
	
	CONSTRAINT PK_NUM PRIMARY KEY (EMP_NUM)
);

INSERT INTO AB1_2 VALUES ('정민수', 2019150, 'minsoo_sung@tmax.co.kr', '010-2301-5625', 5138, TO_DATE('1992-09-29', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('진재혁', 2018139, 'jaehyeok_jin@tmax.co.kr', '010-5062-9197', 5021, TO_DATE('1992-08-21', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('정춘순', 2019268, 'chungsun_jeong@tmax.co.kr', '010-9957-1931', 5062, TO_DATE('1994-10-21', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('김민기', 2020015, 'mingi_kim@tmax.co.kr', '010-8555-9387', '', TO_DATE('1995-03-31', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('김상윤', 2020365, 'sangyoon_kim@tmax.co.kr', '010-9100-8450', 5093, TO_DATE('1992-08-01', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('김혜진', 2020085, 'hyejin_kim@tmax.co.kr', '010-2090-9215', 5100, TO_DATE('1994-09-29', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('김민지', 2020038, 'minji_kim@tmax.co.kr', '010-6348-7983', 5096, TO_DATE('1997-04-26', 'YYYY-MM-DD'));
INSERT INTO AB1_2 VALUES ('한주형', 2020428, 'joohyeong_han@tmax.co.kr', '010-7111-4604', 5098, TO_DATE('1988-10-10', 'YYYY-MM-DD'));



CREATE TABLE ACCOUNTING
(
	EMP_NUM   NUMBER(7) NOT NULL,
	SALARY	  NUMBER(8),
	
	CONSTRAINT PK_NUM2 PRIMARY KEY (EMP_NUM)
);

INSERT INTO ACCOUNTING VALUES (2017100, 75000000);
INSERT INTO ACCOUNTING VALUES (2017123, 68000000);
INSERT INTO ACCOUNTING VALUES (2018139, 65000000);
INSERT INTO ACCOUNTING VALUES (2018140, 65000000);
INSERT INTO ACCOUNTING VALUES (2018141, 65000000);
INSERT INTO ACCOUNTING VALUES (2018250, 65000000);
INSERT INTO ACCOUNTING VALUES (2018340, 60000000);
INSERT INTO ACCOUNTING VALUES (2018550, 62000000);
INSERT INTO ACCOUNTING VALUES (2019080, 63000000);
INSERT INTO ACCOUNTING VALUES (2019150, 63000000);
INSERT INTO ACCOUNTING VALUES (2019200, 63000000);
INSERT INTO ACCOUNTING VALUES (2019268, 55000000);
INSERT INTO ACCOUNTING VALUES (2019320, 62000000);
INSERT INTO ACCOUNTING VALUES (2019425, 62000000);
INSERT INTO ACCOUNTING VALUES (2020015, 48000000);
INSERT INTO ACCOUNTING VALUES (2020020, 50000000);
INSERT INTO ACCOUNTING VALUES (2020038, 40000000);
INSERT INTO ACCOUNTING VALUES (2020050, 58000000);
INSERT INTO ACCOUNTING VALUES (2020060, 58000000);
INSERT INTO ACCOUNTING VALUES (2020085, 54000000);
INSERT INTO ACCOUNTING VALUES (2020300, 52000000);
INSERT INTO ACCOUNTING VALUES (2020365, 63000000);
INSERT INTO ACCOUNTING VALUES (2020400, 52000000);
INSERT INTO ACCOUNTING VALUES (2020428, 75000000);
INSERT INTO ACCOUNTING VALUES (2020520, 70000000);


COMMIT;

SELECT * FROM AB1_2;
SELECT * FROM ACCOUNTING;

SELECT * FROM AB1_2 LEFT JOIN ACCOUNTING ON AB1_2.EMP_NUM = ACCOUNTING.EMP_NUM;
