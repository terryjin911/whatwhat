import React, { useState, useEffect } from "react";

// 라우팅으로 정해져있는 컴포넌트로 이동가능
// 사용하려면
import { useHistory, Link } from "react-router-dom";

import TopHeader from "../../component/TopHeader";
import Footer from "../../component/Footer";

import axios from "axios";

const List = () => {
  let history = useHistory();

  //해당 컴포넌트에서 사용할 예약목록 useState
  const [reserveList, setReserveList] = useState([]);

  //컴포넌트가 최초 로딩될 때만 실행
  useEffect(() => {
    const apiUrl = "http://localhost:8000/api/booking/";

    axios
      .get(apiUrl)
      .then((response) => {
        console.log("조회완료 데이터: ", response.data);

        setReserveList(response.data);
      })
      .catch((response) => {
        console.error(response);
      });
  }, []);

  return (
    <div>
      <h1>예약내역</h1>

      {reserveList.map((item, i) => {
        return (
          <React.Fragment key={item.id}>
            <div>
              <Link to={`/booking/detail/${item.id}`}>
                {item.id}|{item.room}|{item.data_from}|{item.data_to}
              </Link>
            </div>
          </React.Fragment>
        );
      })}

      <div>
        <h1>디테일</h1>
      </div>
    </div>
  );
};

export default List;
