import React, { useState, useEffect } from "react";

// 라우팅으로 정해져있는 컴포넌트로 이동가능
// 사용하려면
import { useHistory, Link } from "react-router-dom";

import TopHeader from "../../component/TopHeader";
import Footer from "../../component/Footer";

import axios from "axios";

const Detail = (props) => {
  let history = useHistory();

  let id = props.match.params.id;

  //단일 예약정보 관련 userSTate
  const [reserve, setReserve] = useState({});

  //컴포넌트가 최초 실행될때만 실행
  useEffect(() => {
    const apiUrl = `http://localhost:8000/api/booking/${id}`;

    axios
      .get(apiUrl)
      .then((response) => {
        console.log("단일예약 데이터: ", response.data);

        setReserve(response.data);
      })
      .catch((response) => {
        console.error(response);
      });
  }, []);

  //예약정보 데이터 바인딩 처리함수 event e!
  const onReserveChange = (e) => {
    setReserve({ ...reserve, [e.target.name]: e.target.value });
  };

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

    const apiUrl = `http://localhost:8000/api/booking/${id}/`;

    axios
      .patch(apiUrl, reserve)
      .then((response) => {
        alert("수정완료");
        history.push("List");
      })
      .catch((response) => {
        console.error(response);
      });
  };

  //데이터 삭제처리
  const onDataDelete = () => {
    const apiUrl = `http://localhost:8000/api/booking/${id}/`;

    axios
      .delete(apiUrl, reserve)
      .then((response) => {
        alert("삭제완료");
        history.push("List");
      })
      .catch((response) => {
        console.error(response);
      });
  };

  const onMoveList = () => {
    history.push("List");
  };

  return (
    <div>
      <div>
        <TopHeader />
        <h1>
          예약 정보확인 : 예약번호 : {id} - {reserve.room}
        </h1>

        <div>
          <table>
            <tbody>
              <tr>
                <td>예약고객번호</td>
                <td>
                  <input
                    type="text"
                    name="subscriber"
                    defaultValue={reserve.subscriber}
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
                    defaultValue={reserve.room}
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
                    defaultValue={reserve.date_from}
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
                    defaultValue={reserve.date_to}
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
                    defaultValue={reserve.note}
                    onChange={(e) => onReserveChange(e)}
                  />
                </td>
              </tr>

              {/* 라우팅기반 페이지이동 useHistory */}
              <tr>
                <td colSpan="2">
                  <button onClick={() => onDataSave()}> 수정 </button>
                  <button onClick={() => history.goBack()}> 뒤로가기 </button>
                  <button onClick={() => onMoveList()}> 목록이동 </button>
                  <button onClick={() => onDataDelete()}> 삭제 </button>
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

export default Detail;
