import Link from "next/link";
import React from "react";

const Vacanse = ({ data }) => {
  const { id, title, company, timeago } = data;
  return (
    <Link href={`/${id}`}>
      {title} - {company} - {timeago}
    </Link>
  );
};

export default Vacanse;
