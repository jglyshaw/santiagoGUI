n = Neuron(185,'t');
nodes = n.nodes;
segments = sbfsem.render.Segment(n);

 for i = 1:height(segments.segmentTable)
     xyz = cell2mat(segments.segmentTable{i, 'XYZum'});
     line(xyz(:,1), xyz(:,2), xyz(:,3),...
          'Marker', '.', 'MarkerSize', 2,...
          'LineWidth', 1, 'Color', 'k',...
          'Tag', num2str(i));
     hold on
 end

 
 %-------------------------------------%
 
 
  for i = 1:height(segments.segmentTable)
                
                % Generate cylinder coordinates with correct radii
                radii = cell2mat(segments.segmentTable{i, 'Rum'});
       
                [X, Y, Z] = cylinder(radii);
                % Translate the cylinder points by annotation XYZ
                xyz = cell2mat(segments.segmentTable{i, 'XYZum'});
                Z = repmat(xyz(:, 3), [1, size(Z, 2)]);
                % The PickableParts setting ensures surfaces are invisible
                % in datacursormode.
                s = surf(X+xyz(:, 1), Y+xyz(:,2), Z,...
                    'FaceAlpha', 0.3,...`
                    'EdgeColor', 'none',...
                    'PickableParts', 'none',...
                    'Tag', ['s', num2str(i)]);
          
          
                hold on
  end