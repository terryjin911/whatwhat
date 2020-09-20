import React from "react";
import "./App.css";

// 페이지 라우팅을 위한 어쩌구
import { Route } from "react-router-dom";

import Main from "./page/Main";

import Regist from "./page/booking/Regist";
import List from "./page/booking/List";
import Detail from "./page/booking/Detail";

function App() {
  return (
    // /는 파라메터라고 함. 파라메터를 추출한다^ㅇ^
    <div className="App">
      <Route path="/" component={Main} exact={true} />
      <Route path="/booking/regist/" component={Regist} />
      <Route path="/booking/list" component={List} />
      <Route path="/booking/detail/:id" component={Detail} />
    </div>
  );
}

export default App;
