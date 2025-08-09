import "./AssistantSpeechIndicator.css";


const AssistantSpeechIndicator = ({ isSpeaking }) => {
  return (
    <div className="assistant-speech-editor">
      <div
        className={`speech-indicator ${
          isSpeaking ? "speaking" : "not-speaking"
        }`}
      ></div>
      <p className="speech-status">
        {isSpeaking ? "Assistant Speaking" : "Assistant Not Speaking"}
      </p>
    </div>
  );
};

export default AssistantSpeechIndicator