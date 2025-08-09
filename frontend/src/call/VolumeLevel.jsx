const numBars = 10;

const VolumeLevel = ({ volume }) => {
  return (
    <div className="volume-level">
      <div className="volume-bars">
        {Array.from({ length: numBars }, (_, i) => {
          return (
            <div
              key={i}
              className={`volume-bar ${i / numBars < volume ? "active" : ""}`}
            ></div>
          );
        })}
      </div>
    </div>
  );
};

export default VolumeLevel