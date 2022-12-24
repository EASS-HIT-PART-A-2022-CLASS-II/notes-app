import { MdDeleteForever, MdEditNote } from "react-icons/md";

const Note = ({ id, text, date, handleDeleteNote }) => {
  return (
    <div className="note">
      <div className="note-header">
        <span>{text}</span>
        <MdEditNote className="edit-icon" size="1.3em" />
      </div>
      <div className="note-footer">
        <small>{date}</small>
        <MdDeleteForever
          onClick={() => handleDeleteNote(id)}
          className="delete-icon"
          size="1.3em"
        />
      </div>
    </div>
  );
};

export default Note;
