import { MdDeleteForever, MdEditNote } from "react-icons/md";
import { useState } from "react";

const Note = ({ id, text, date, handleDeleteNote, handleEditNote }) => {
  const [editMode, setEditMode] = useState(false);
  const [editText, setEditText] = useState(text);

  const characterLimit = 200;

  const handleChange = (event) => {
    if (characterLimit - event.target.value.length >= 0) {
      setEditText(event.target.value);
    }
  };

  const handleSaveClick = () => {
    if (editText.trim().length > 0) {
      const updatedDate = new Date();
      const update = {
        text: editText,
        date: updatedDate.toLocaleDateString(),
      };
      handleEditNote(id, update);
      setEditMode(false);
    }
  };

  return (
    <div className="note-container">
      <div className={`${(!editMode && "note") || (editMode && "edit-mode")}`}>
        <div className="note-header">
          <span>{text}</span>
          <MdEditNote
            onClick={() => setEditMode(true)}
            className="edit-icon"
            size="1.3em"
          />
        </div>
        <div className="note-footer">
          <small>{date}</small>
          <MdDeleteForever
            onClick={() => {
              handleDeleteNote(id);
            }}
            className="delete-icon"
            size="1.3em"
          />
        </div>
      </div>
      <div
        className={`${(editMode && "note edit") || (!editMode && "edit-mode")}`}
      >
        <textarea
          rows="8"
          cols="10"
          value={editText}
          onChange={handleChange}
        ></textarea>
        <div className="note-footer">
          <small>{characterLimit - editText.length} Remaining</small>
          <div className="buttons">
            <button className="save edit-btn" onClick={handleSaveClick}>
              Save
            </button>
            <button
              className="save"
              onClick={() => {
                setEditMode(false);
              }}
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Note;
