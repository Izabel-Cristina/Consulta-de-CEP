# Consulta de CEP
<p> Esse projeto foi desenvolvido em Python, utilizei as bibliotecas 'Requests e Json' para integrar a API no código do projeto, <br>
  e a biblioteca PySimpleGUI para criar a interface do projeto. 
  A API integrada foi da Via Cep.
  </p>
  <h3>
  Interface: </h3>
  
![Interface](https://user-images.githubusercontent.com/115845859/202256820-8c2860d1-9dd7-4e3c-8b36-49f61d5d0d4c.png)
<p>  A interface é composta pelo campo que informa o cep, o botão de consultar e o botão de cancelar.</p>
  
  <h3>Funcionalidade:</h3>
  
  Ao informar o cep e clicar no botão 'consultar', temos as informações de endereço de acordo com cep informado.<br> 
  As informações são:CEP informado, Logradouro, complemento, cidade, bairro e UF.
![interface com cep](https://user-images.githubusercontent.com/115845859/202259686-294ec675-e374-4f82-9af9-e87f2180f588.PNG)

<p> Se o usuário informar o cep usando caracteres como  "-" já que no CEP é utilizado como padrão ou até mesmo "." o sistema<br> 
 reconhece e busca normalmente as informações.</p>
  
![interface com caractere](https://user-images.githubusercontent.com/115845859/202280213-754c2c94-0035-483c-9123-b0fd51e7ebf1.PNG)

<p>Se caso o usuário informar um CEP inexistente aparece um aviso de erro.</p>

![cep inexistente](https://user-images.githubusercontent.com/115845859/202281584-57fb6b63-d3cb-4110-81e8-a048641b763e.PNG)

<p> Ao clicar em 'cancelar' o sistema é finalizado. </p>

<h4> Linguagem de programação utilizada:</h4>
<p> Python; </p>
<h4> Bibliotecas utilizadas:</h4> 
<p> PySimpleGUI;</p>
<p> Json;</p>
<p> Requests;</p>
