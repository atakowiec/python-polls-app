import React from "react";
import { Option } from "@/types/polls";

interface OptionListProps {
  options: Option[];
  onVote: (optionId: number) => void;
  disabled?: boolean;
}

const OptionList: React.FC<OptionListProps> = ({ options, onVote, disabled }) => {
  const totalVotes = options.reduce((sum, option) => sum + option.votes, 0);

  return (
    <ul className="space-y-3">
      {options.map((option) => {
        const percentage = totalVotes === 0 ? 0 : (option.votes / totalVotes)*100;

        return (
          <li
            key={option.id}
            className="relative border rounded overflow-hidden group"
          >
            <div
              className="absolute top-0 left-0 h-full bg-blue-200 transition-all duration-500 ease-out"
              style={{ width: `${percentage}%` }}
            />

            <div className="relative z-10 flex justify-between items-center p-3 hover:bg-black/5 transition-colors">
              <span className="font-medium text-gray-800">{option.text}</span>

              <div className="flex items-center space-x-4">
                <span className="text-sm text-gray-800 font-mono">
                  {Math.round(percentage*10)/10}%
                </span>

                <span className="text-gray-700 w-8 text-right">
                  {option.votes}
                </span>

                <button
                  className="bg-blue-600 text-white px-3 py-1 text-sm rounded hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm"
                  onClick={() => onVote(option.id)}
                  disabled={disabled}
                >
                  Vote
                </button>
              </div>
            </div>
          </li>
        );
      })}
    </ul>
  );
};

export default OptionList;