import React, { useState } from "react";

// 라우팅으로 정해져있는 컴포넌트로 이동가능
// 사용하려면
import { useHistory } from "react-router-dom";

import TopHeader from "../../component/TopHeader";
import Footer from "../../component/Footer";

import axios from "axios";

const Regist = () => {
  // useHistory 컴포넌트에서의 자유로운 페이지 이동가능 기능 제공
  //
  let history = useHistory();

  // 목록페이지로 이동
  // 헐 의외로 존나쉽네
  const onMoveList = () => {
    history.push("List");
  };

  // 어떤 속성명으로 하는지 = python-Django DAY5 작성했던거 참고 - swagger로 들어가서 GET(booking)->ExampleValue 참고
  // yarn start해서 [예약고객번호 : 1 ] 이미 작성되어있는 부분은 건들면 에러가 뜨면서 완료가 뜨지않음
  // 걍 디폴트로 넣어져있는 값은 건들지말도록하자 ^ㅇ^
  const [reserve, setReserve] = useState({
    subscriber: 1,
    date_from: "",
    date_to: "",
    room: "",
    note: "",
  });

  //예약정보 데이터 바인딩 처리함수 event e!
  const onReserveChange = (e) => {
    setReserve({ ...reserve, [e.target.name]: e.target.value });
  };

  //데이터 백엔드 저장처리 함수
  const onDataSave = () => {
    // 유효성검사 만약 reserve에 subscriber가 비어있으면
    if (reserve.subscriber == "") {
      alert("예약자 정보를 입력해주세요.");
      return false;
    }

    if (reserve.room == "") {
      alert("예약룸 정보를 입력해주세요.");
      return false;
    }

    const apiUrl = "http://localhost:8000/api/booking/";

    axios
      .post(apiUrl, reserve)
      .then((response) => {
        console.log("등록완료 데이터: ", response.data);
        alert("등록완료");
        history.push("List");
      })
      .catch((response) => {
        console.error(response);
      });
  };

  //데이터 보낼때는 post를 써야함
  //콜을 =>{} 여기로 받음

  return (
    <div>
      <div>
        <TopHeader />
        <h1>예약등록</h1>

        <div>
          <table>
            <tbody>
              <tr>
                <td>예약고객번호</td>
                <td>
                  <input
                    type="text"
                    name="subscriber"
                    value={reserve.subscriber}
                    onChange={(e) => onReserveChange(e)}
                  />
                </td>
              </tr>

              <tr>
                <td>예약룸</td>
                <td>
                  <input
                    type="text"
                    name="room"
                    value={reserve.room}
                    onChange={(e) => onReserveChange(e)}
                  />
                </td>
              </tr>

              <tr>
                <td>시작일</td>
                <td>
                  <input
                    type="text"
                    name="date_from"
                    value={reserve.date_from}
                    onChange={(e) => onReserveChange(e)}
                  />
                </td>
              </tr>

              <tr>
                <td>종료일</td>
                <td>
                  <input
                    type="text"
                    name="date_to"
                    value={reserve.date_to}
                    onChange={(e) => onReserveChange(e)}
                  />
                </td>
              </tr>

              <tr>
                <td>코멘트</td>
                <td>
                  <input
                    type="text"
                    name="note"
                    value={reserve.note}
                    onChange={(e) => onReserveChange(e)}
                  />
                </td>
              </tr>

              {/* 라우팅기반 페이지이동 useHistory */}
              <tr>
                <td colSpan="2">
                  <button onClick={() => onDataSave()}> 등록 </button>
                  <button onClick={() => history.goBack()}> 뒤로가기 </button>
                  <button onClick={() => onMoveList()}> 목록이동 </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <Footer />
      </div>
    </div>
  );
};

export default Regist;
