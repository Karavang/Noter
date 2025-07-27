import Link from "next/link";
import React from "react";

const Vacanse = ({ data }) => {
  const { id, title, company, timeago } = data;
  return (
    <Link
      className="vacanse-link"
      href={`/${id}`}
    >
      {title} - {company} - {timeago}
    </Link>
  );
};

export default Vacanse;
