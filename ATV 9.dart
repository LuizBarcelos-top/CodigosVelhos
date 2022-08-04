//Luiz Augusto - 2920481911013

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

const request = "https://api.hgbrasil.com/finance";

//Alteração de Cores
//Alteração de nomes
//Alteração de tamanhos

void main() async {
  print(await pegarDados());
  runApp(
    MaterialApp(
      //home: Container(),
      home: Home(),
    ),
  );
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String nomeIbovespa;
  String localIbovespa;
  String pontosIbovespa;
  String variacaoIbovespa;

  String nomeNasdaq;
  String localNasdaq;
  String pontosNasdaq;
  String variacaoNasdaq;

  String nomeNikkei;
  String localNikkei;
  String variacaoNikkei;

  String nomeCac;
  String localCac;
  String variacaoCac;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text("Bolsa de Valores Internacional"),
        backgroundColor: Colors.blueAccent,
        centerTitle: true,
      ),
      body: FutureBuilder(
        future: pegarDados(),
        builder: (context, snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.none:
            case ConnectionState.waiting:
              return Center(
                child: Text(
                  "Carregando Dados...",
                  style: TextStyle(
                    color: Colors.red,
                    fontSize: 24,
                  ),
                  textAlign: TextAlign.center,
                ),
              );
            default:
              if (snapshot.hasError) {
                return Center(
                  child: Text(
                    "Erro ao Carregar os Dados",
                    style: TextStyle(
                      color: Colors.red,
                      fontSize: 24,
                    ),
                    textAlign: TextAlign.center,
                  ),
                );
              } else {
                nomeIbovespa = snapshot.data["results"]["stocks"]["IBOVESPA"]
                        ["name"]
                    .toString();
                localIbovespa = snapshot.data["results"]["stocks"]["IBOVESPA"]
                        ["location"]
                    .toString();
                pontosIbovespa = snapshot.data["results"]["stocks"]["IBOVESPA"]
                        ["points"]
                    .toString();
                variacaoIbovespa = snapshot.data["results"]["stocks"]
                        ["IBOVESPA"]["variation"]
                    .toString();
                //nasdaq
                nomeNasdaq = snapshot.data["results"]["stocks"]["NASDAQ"]
                        ["name"]
                    .toString();
                localNasdaq = snapshot.data["results"]["stocks"]["NASDAQ"]
                        ["location"]
                    .toString();
                pontosNasdaq = snapshot.data["results"]["stocks"]["NASDAQ"]
                        ["points"]
                    .toString();
                variacaoNasdaq = snapshot.data["results"]["stocks"]["NASDAQ"]
                        ["variation"]
                    .toString();
                //nikkei
                nomeNikkei = snapshot.data["results"]["stocks"]["NIKKEI"]
                        ["name"]
                    .toString();
                localNikkei = snapshot.data["results"]["stocks"]["NIKKEI"]
                        ["location"]
                    .toString();

                variacaoNikkei = snapshot.data["results"]["stocks"]["NIKKEI"]
                        ["variation"]
                    .toString();

                //CAC
                nomeCac = snapshot.data["results"]["stocks"]["CAC"]["name"]
                    .toString();
                cacLocal = snapshot.data["results"]["stocks"]["CAC"]["location"]
                    .toString();

                variacaoCac = snapshot.data["results"]["stocks"]["CAC"]
                        ["variation"]
                    .toString();

                return SingleChildScrollView(
                  padding: EdgeInsets.all(10),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Image.asset(
                        "images/bolsa.jpg",
                        fit: BoxFit.cover,
                        height: 100,
                      ),
                      Divider(),
                      construirTexto(nomeIbovespa),
                      construirTexto(localIbovespa),
                      construirTexto(pontosIbovespa),
                      construirTexto(variacaoIbovespa),
                      Divider(),
                      construirTexto(nomeNasdaq),
                      construirTexto(localNasdaq),
                      construirTexto(pontosNasdaq),
                      construirTexto(variacaoNasdaq),
                      Divider(),
                      construirTexto(nomeNikkei),
                      construirTexto(localNikkei),
                      construirTexto(variacaoNikkei),
                      Divider(),
                      construirTexto(nomeCac),
                      construirTexto(cacLocal),
                      construirTexto(variacaoCac),
                    ], //children column
                  ),
                );
              } //if else
          } //swtich
        }, //builder
      ),
    );
  }
}

Future<Map> pegarDados() async {
  http.Response response = await http.get(request);
  return json.decode(response.body);
}

Widget construirTexto(String texto) {
  return Text(
    texto,
    textAlign: TextAlign.center,
    style: TextStyle(
      color: Colors.blueAccent,
      fontSize: 25,
    ),
  );
}

