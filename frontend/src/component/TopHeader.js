import React from "react";

import { Link } from "react-router-dom";

const TopHeader = () => {
  return (
    <div>
      <span>
        <Link to="/">홈 |</Link>
        <Link to="/booking/list">예약목록 |</Link>
        <Link to="/booking/regist">예약하기 |</Link>
      </span>
    </div>
  );
};

export default TopHeader;
