import 'package:flutter/material.dart';

//Luiz Augusto - 2920481911013

//a) Restrição de numero negativo de pessoas
//b) Mensagem vai mundando de cor conforme o umero aumenta
//c) Indicação de lotação máxima


void main() {
  runApp(
    MaterialApp(
      title: "Contador de alunos Fatec Ferraz",
      debugShowCheckedModeBanner: false,
      home: Home()
    ),
  ); // runApp
} // main

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _pessoas = 0;
  String _mensagem = "Pode Entrar!";
  int fontMensagem = 30;
  var _cor = Colors.green[700];

  _alteraContador(int i){
    setState(() {
      _pessoas += i;
      _alterarCor();
    });
  }

  _alterarMensagem(){
    if(_pessoas < 50){
      setState(() {
        _mensagem = "Pode Entrar!";
      });
    }
    else {
      setState(() {
        _mensagem = "Lotado! Por favor aguarde!!";
      });
    }
  }

  double _alterarFont(){
    return (_pessoas == 50) ? 25 : 30;
  }

  _alterarCor(){
    if(_pessoas < 20){
      setState(() {
        _cor = Colors.green[700];
      });
    } else if (_pessoas < 40){
      setState(() {
        _cor = Colors.yellow;
      });
    } else {
      _cor = Colors.redAccent[700];
    }
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
          Image.asset(
          "images/fatec2.jpg",
          fit: BoxFit.cover,
          height: 1000,
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Padding(
              padding: EdgeInsets.fromLTRB(20, 50, 20, 50),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    "Lotação máxima: 50",
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 20
                    ),
                  )
                ]
              ),
            ),
          ],
        ),
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Pessoas: " + _pessoas.toString(),
              style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: EdgeInsets.all(20),
                  child: FlatButton(
                    child: Text(
                      "+1",
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 40,
                      ),
                    ),
                    onPressed: (){
                      if(_pessoas < 50){
                        _alteraContador(1);
                        print(_pessoas);
                      }
                      _alterarMensagem();
                    },
                  ),
                  
                ),
                Padding(
                  padding: EdgeInsets.all(20),
                  child: FlatButton(
                    child: Text(
                      "-1",
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 40,
                      ),
                    ),
                    onPressed: (){
                      if(_pessoas > 0){
                        _alteraContador(-1);
                      }
                      _alterarMensagem();
                    },
                  ),
                ),
              ],
            ),
            Text(
              _mensagem,
              style: TextStyle(
                color: _cor,
                fontWeight: FontWeight.bold,
                fontStyle: FontStyle.italic,
                fontSize: _alterarFont(), 
              ),
            ),
          ],
        ),
      ],
    );
  }
}
