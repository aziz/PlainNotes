# Tables

| First Header | Second Header | Third Header |
|--------------|---------------|--------------|
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |
|              |               |              |

| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

| Name | Phone |
| Name | Phone |
| _    |       |

|    Name   |   Phone   |
|-----------|-----------|
| Anna      | 123456789 |
| Alexander | 987654321 |
| _         |           |

| Name | Phone |
|======|=======|
| _    |       |

|    Name   |   Phone   |
|===========|===========|
| Anna      | 123456789 |
|-----------|-----------|
| Alexander | 987654321 |
|-----------|-----------|
| _         |           |

|    Name   |   |   Phone   |
|-----------|---|-----------|
| Anna      |   | 123456789 |
| Alexander |   | 987654321 |
|           | _ |           |

|    Name   | Age |   Phone   |
|-----------|-----|-----------|
| Anna      |  32 | 123456789 |
| Alexander |  28_| 987654321 |

|    Name   |   Phone   | Age |             Position             |
|-----------|-----------|-----|----------------------------------|
| Anna      | 123456789 |  32 | Senior Software                  |
|           |           |     | Engineer_                        |
|-----------|-----------|-----|----------------------------------|
| Alexander | 987654321 |  28 | Senior Software Testing Engineer |

| column 1 | column 2 | column 3 |
| <<<<<<<< | >>>>>>>> | ######## |
|----------|----------|----------|
| 1        |    row 1 |    c1    |
| 2        |    row 2 |    c2    |
| 3        |    row 3 |    c3    |
|          |          |          |

| Unordered  List |   Order List  |
|-----------------|---------------|
| - item 1        | # item 1      |
|   - subitem 1   |   # subitem 1 |
|   - subitem 2   | # item 2      |
| - item 2        |   # subitem 2 |

|   *First Header*  | **Second Header** | ~~Third Header~~ |
|-------------------|-------------------|------------------|
| `Content Cell`    | [Content Cell][2] | ![Image][3]      |
| http://google.com | <me@ssd.com>      | some text        |

| Unordered  List | Order List |
|-----------------|------------|
| C++             | D--        |
| E::             | X==        |
|                 |            |

### Supported Syntaxes

**Simple**

|    Name   | Age |
|-----------|-----|
| Anna      |  20 |
| Alexander |  27 |

**EmacsOrgMode**

|    Name   | Age |
|-----------+-----|
| Anna      |  20 |
| Alexander |  27 |

**Pandoc Grid Tables**

+-----------+-----+
|    Name   | Age |
+===========+=====+
| Anna      |  20 |
+-----------+-----+
| Alexander |  27 |
+-----------+-----+

**Pandoc Pipe tables**

**Multi Markdown/Pandoc Pipe tables**

Alignment:

|    Name   | Phone | Age Column |
| :-------- | :---: | ---------: |
| Anna      |   12  |         20 |
| Alexander |   13  |         27 |

| Right | Left | Default | Center |
| ----: | :--- | ------- | :----: |
|    12 | 12   |      12 |   12   |
|   123 | 123  |     123 |  123   |
|     1 | 1    |       1 |   1    |

**RestructuredText**

|    Name   | Age |
+-----------+-----+
| Anna      |  20 |
| Alexander |  27 |

### Column spanning in multimarkdown tables

| First Header  | Second Header | Third Header         |
| :------------ | :-----------: | -------------------: |
| First row     | Data          | Very long data entry |
| Second row    | **Cell**      | *Cell*               |
| Third row     | Cell that spans across two columns  ||
[Table caption, works as a reference][section-mmd-tables-table1] 

| Column 1 | Column 2 | Column 3 | Column 4 |
| -------- | :------: | -------- | -------- |
| No span  | Span across three columns    |||

|               |          Grouping           ||
| First Header  | Second Header | Third Header |
| ------------  | :-----------: | -----------: |
| Content       |          *Long Cell*        ||
| Content       |   **Cell**    |         Cell |
|               |               |              |
| New section   |     More      |         Data |
| And more      |            And more         ||
[Prototype table][]

### table with spacing before and after
*before*

  | Name | Phone |
  | Name | Phone |
  | _    |       |

*after*

| Name | Phone |   
| Name | Phone |   
| _    |       |   

  | Name | Phone |   
  | Name | Phone |   
  | _    |       |  

## NOT SUPPORTED 

### Tables with no pipe at the begining or end

First Header | Second Header | Third Header
------------ | ------------- | ------------
Content Cell | Content Cell  | Content Cell
Content Cell | Content Cell  | Content Cell

First Header | Second Header | Third Header
:----------- | :-----------: | -----------:
Left         | Center        | Right
Left         | Center        | Right
